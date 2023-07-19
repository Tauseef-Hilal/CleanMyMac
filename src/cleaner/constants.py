from getpass import getuser

LIB_PATH = f"/Users/{getuser()}/Library"
CACHE_DIR_PATH = f"{LIB_PATH}/Caches"

CONTAINERS_DIR_PATH = f"{LIB_PATH}/Containers"
CONTAINER_SUFFIX = "Data/Library/Caches"

APPLICATION_SUPPORT_DIR = f"{LIB_PATH}/Application Support"
APPLICATION_SUPPORT_SUFFIX = "Cache"

XCODE_DERIVED_DATA_DIR = f"{LIB_PATH}/Developer/Xcode/DerivedData"
IOS_DEVICE_LOGS_DIR = f"{LIB_PATH}/Developer/Xcode/iOS Device Logs"

USER_LOGS_DIR = f"{LIB_PATH}/Logs"
