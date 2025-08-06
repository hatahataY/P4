import subprocess
import os
import sys

def build_p4_components(root_dir: str) -> tuple[bool, str, str]:
    try:
        # 1. Build PI (Protocol Independent)
        pi_dir = os.path.join(root_dir, "PI")
        build_pi_dir = os.path.join(root_dir, "build", "PI")
        os.makedirs(build_pi_dir, exist_ok=True) # ビルドディレクトリが存在しない場合は作成
        # autogen.sh
        if not os.path.exists(os.path.join(pi_dir, "configure")):
            subprocess.run(["./autogen.sh"], cwd=pi_dir, check=True)
        # configure
        if not os.path.exists(os.path.join(build_pi_dir, "config.h")):
            local_libs_path = os.path.join(root_dir, "install", "lib")

            ldflags = f"-L{local_libs_path} {os.environ.get('LDFLAGS', '')}"

            subprocess.run([
                os.path.join(pi_dir, "configure"),
                f"--prefix={root_dir}/install",
                f"--libdir={root_dir}/install/lib",
                f"--bindir={root_dir}/install/bin",
                "--with-proto"
            ], cwd=build_pi_dir, check=True)
        # make
        subprocess.run(["make", "install", "-j", str(os.cpu_count())], cwd=build_pi_dir, check=True)

        # 2. Build bmv2 (behavioral-model)
        bmv2_dir = os.path.join(root_dir, "behavioral-model")
        build_bmv2_dir = os.path.join(root_dir, "build", "behavioral-model")
        os.makedirs(build_bmv2_dir, exist_ok=True) # ビルドディレクトリが存在しない場合は作成
        # autogen.sh
        if not os.path.exists(os.path.join(bmv2_dir, "configure")):
            subprocess.run(["./autogen.sh"], cwd=bmv2_dir, check=True)
        # configure
        if not os.path.exists(os.path.join(build_bmv2_dir, "config.h")):
            pi_libs_path = os.path.join(build_pi_dir, "proto", "frontend", ".libs")
            pi_server_libs_path = os.path.join(build_pi_dir, "proto", "server", ".libs")
            pi_src_libs_path = os.path.join(build_pi_dir, "src", ".libs")
            pi_include_path = os.path.join(pi_dir, "include")
            pi_proto_frontend_path = os.path.join(pi_dir, "proto", "frontend")
            pi_proto_server_path = os.path.join(pi_dir, "proto", "server")
            bmv2_include_path = os.path.join(build_bmv2_dir, "include")
            local_libs_path = os.path.join(root_dir, "install", "lib")

            ldflags = f"-L{pi_libs_path} -L{pi_server_libs_path} -L{pi_src_libs_path} {os.environ.get('LDFLAGS', '')}"
            cppflags = f"{os.environ.get('CPPFLAGS', '')} -I{pi_include_path} -I{pi_proto_frontend_path} -I{pi_proto_server_path} -I{bmv2_include_path}"

            subprocess.run([
                os.path.join(bmv2_dir, "configure"),
                f"LDFLAGS={ldflags}",
                f"CPPFLAGS={cppflags}",
                f"--prefix={root_dir}/install",
                f"--libdir={root_dir}/install/lib",
                f"--bindir={root_dir}/install/bin",
                "--with-thrift",
                "--with-pi"
            ], cwd=build_bmv2_dir, check=True)
        # make
        subprocess.run(["make", "install", "-j", str(os.cpu_count())], cwd=build_bmv2_dir, check=True)

        # 3. Build p4c (P4 Compiler)
        p4c_dir = os.path.join(root_dir, "p4c")
        build_p4c_dir = os.path.join(root_dir, "build", "p4c")
        os.makedirs(build_p4c_dir, exist_ok=True) # ビルドディレクトリが存在しない場合は作成
        # cmake
        if not os.path.exists(os.path.join(build_p4c_dir, "CMakeCache.txt")):
            subprocess.run([
                "cmake", p4c_dir,
                "-DENABLE_BMV2=ON",
                "-DENABLE_EBPF=OFF",
                "-DENABLE_P4TC=OFF",
                "-DENABLE_UBPF=OFF",
                "-DENABLE_DPDK=OFF",
                "-DENABLE_P4C_GRAPHS=OFF",
                "-DENABLE_P4FMT=OFF",
                "-DENABLE_P4TEST=OFF",
                "-DP4C_USE_PREINSTALLED_ABSEIL=ON",
                f"--install-prefix={root_dir}/install"
            ], cwd=build_p4c_dir, check=True)
        # make
        subprocess.run(["make", "install", "-j4"], cwd=build_p4c_dir, check=True) # p4c は -j4 指定

        dockerfile_path = f"{root_dir}/../clab-node/Dockerfile.node"
        context_path = f"{root_dir}/.."

        return True, dockerfile_path, context_path
    except subprocess.CalledProcessError as e:
        print(f"Error during P4 component build: {e}", file=sys.stderr)
        print(f"Command '{' '.join(e.cmd)}' failed with exit code {e.returncode}.", file=sys.stderr)
        return False, "", ""
    except Exception as e:
        print(f"An unexpected error occurred during P4 component build: {e}", file=sys.stderr)
        return False, "", ""
