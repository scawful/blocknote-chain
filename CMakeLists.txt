cmake_minimum_required(VERSION 3.10)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

project(blocknote-chain VERSION 0.40)

set(Boost_USE_STATIC_LIBS ON)
find_package(Boost REQUIRED)
include_directories(SYSTEM ${Boost_INCLUDE_DIRS})

if(APPLE)
    set(OPENSSL_INCLUDE_DIR "/usr/local/Cellar/openssl@1.1/1.1.1o/include")
    set(OPENSSL_CRYPTO_LIBRARY "/usr/local/Cellar/openssl@1.1/1.1.1o/lib/libcrypto.dylib")
    set(OPENSSL_SSL_LIBRARY "/usr/local/Cellar/openssl@1.1/1.1.1o/lib/libssl.dylib")
endif()
find_package(OpenSSL REQUIRED)
if(OPENSSL_FOUND)
    if(APPLE)
        include_directories(/usr/local/Cellar/openssl@1.1/1.1.1o/include)
        list(APPEND LIB_LIST /usr/local/Cellar/openssl@1.1/1.1.1o/lib/libssl.dylib)
        list(APPEND LIB_LIST /usr/local/Cellar/openssl@1.1/1.1.1o/lib/libcrypto.dylib)
        message(STATUS "OpenSSL Version: ${OPENSSL_VERSION} ${OPENSSL_INCLUDE_DIR} ${OPENSSL_LIBRARIES}")
    else()
        include_directories(${OPENSSL_INCLUDE_DIR})
        list(APPEND LIB_LIST ${OPENSSL_LIBRARIES})
        message(STATUS "OpenSSL Version: ${OPENSSL_VERSION} ${OPENSSL_INCLUDE_DIR} ${OPENSSL_LIBRARIES}")
    endif()
endif()

add_executable(
  blocknote-chain
  src/main.cc
  src/blocknote/block.cc
  src/blocknote/wallet.cc
  src/blocknote/sha256.cc
)

include_directories(
  blocknote-chain
  include/
)

target_link_libraries(
  blocknote-chain 
  ${BOOST_LIBRARIES} 
  OpenSSL::SSL 
)