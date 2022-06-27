cmake_minimum_required(VERSION 3.10)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

project(blocknote-chain VERSION 0.40)

set(Boost_USE_STATIC_LIBS ON)
find_package(Boost REQUIRED)
include_directories(SYSTEM ${Boost_INCLUDE_DIRS})

find_package(SDL2 REQUIRED)

set(IMGUI_PATH  "src/viewer/lib/imgui")
file(GLOB IMGUI_SOURCES ${IMGUI_PATH}/*.cpp)
add_library("ImGui" STATIC ${IMGUI_SOURCES})
target_include_directories("ImGui" PUBLIC ${IMGUI_PATH})
target_include_directories(ImGui PUBLIC ${SDL2_INCLUDE_DIR})
target_compile_definitions(ImGui PUBLIC IMGUI_IMPL_OPENGL_LOADER_CUSTOM=<SDL2/SDL_opengl.h>  GL_GLEXT_PROTOTYPES=1)

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
  src/blocknote/blockchain.cc
  src/blocknote/commands.cc
  src/blocknote/database.cc
  src/blocknote/network.cc
  src/blocknote/delta.cc
  src/blocknote/network.cc
  src/blocknote/transaction.cc
  src/blocknote/key_pair.cc
  src/blocknote/sha256.cc
  ${IMGUI_PATH}/imgui.cpp 
  ${IMGUI_PATH}/imgui_demo.cpp
  ${IMGUI_PATH}/imgui_draw.cpp 
  ${IMGUI_PATH}/imgui_widgets.cpp
  ${IMGUI_PATH}/backends/imgui_impl_sdl.cpp
  ${IMGUI_PATH}/backends/imgui_impl_sdlrenderer.cpp 
  ${IMGUI_PATH}/misc/cpp/imgui_stdlib.cpp
)

include_directories(
  blocknote-chain
  include/
  ${SDL2_INCLUDE_DIR}
  src/viewer/lib/
  ${Boost_INCLUDE_DIRS}
)

target_link_libraries(
  blocknote-chain 
  ${BOOST_LIBRARIES} 
  ${SDL2_LIBRARIES} 
  ${OPENGL_LIBRARIES} 
  OpenSSL::SSL 
  ImGui 

)