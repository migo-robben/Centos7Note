VULKAN_SDK="/home/migo/DEV_PROJECTS/WSRD/vulkan/1.2.135.0/x86_64"
export VULKAN_SDK
PATH="$VULKAN_SDK/bin:$PATH"
export PATH
LD_LIBRARY_PATH="$VULKAN_SDK/lib:${LD_LIBRARY_PATH:-}"
export LD_LIBRARY_PATH
VK_LAYER_PATH="$VULKAN_SDK/etc/vulkan/explicit_layer.d"
export VK_LAYER_PATH

export PATH="/home/migo/DEV_PROJECTS/COMPILER/gcc-8.3.0/bin/:$PATH" 
export CC="/home/migo/DEV_PROJECTS/COMPILER/gcc-8.3.0/bin/gcc"
export CXX="/home/migo/DEV_PROJECTS/COMPILER/gcc-8.3.0/bin/g++"
export LD_LIBRARY_PATH="/home/migo/DEV_PROJECTS/COMPILER/gcc-8.3.0/lib64:$LD_LIBRARY_PATH"

/home/migo/DEV_PROJECTS/GIT/UnrealEngine/Engine/Binaries/Linux/UE4Editor