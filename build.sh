# 1. Build PI
cd ~/PI
./autogen.sh \
&& ./configure --with-proto \
&& make -j$(nproc)

# 2. Build bmv2
cd ~/behavioral-model
./autogen.sh \
&& ./configure \
     LDFLAGS="-L$(pwd)/../PI/proto/frontend/.libs \
              -L$(pwd)/../PI/proto/server/.libs \
              -L$(pwd)/../PI/src/.libs $LDFLAGS" \
     CPPFLAGS="$CPPFLAGS -I$(pwd)/../PI/include \
              -I$(pwd)/../PI/proto/frontend \
              -I$(pwd)/../PI/proto/server" \
     --with-thrift --with-pi \
&& make -j$(nproc)

# 3. Build p4c
cd ~/p4c
mkdir -p build && cd build \
&& cmake ..
&& make -j4
&& make -j4 check