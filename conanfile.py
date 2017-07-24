from conans import ConanFile, CMake, tools


class ZmqppConan(ConanFile):
    name = "zmqpp"
    description = "0mq 'highlevel' C++ bindings"
    version = "4.1.2"
    license = "Mozilla Public License 2.0"
    url = "https://github.com/gasuketsu/conan-zmqpp"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "txt"
    options = {"build_client": [True, False]}
    default_options = "build_client=False"

    def requirements(self):
        self.requires("libzmq/[>4.1.0]@memsharded/stable")
        if self.options.build_client:
            self.requires("Boost/[>1.58.0]@lasote/stable")

    def configure(self):
        self.options["libzmq"].shared = "True"

    def source(self):
        self.run("git clone https://github.com/zeromq/zmqpp.git")
        self.run("cd zmqpp && git checkout %s" % self.version)
        tools.replace_in_file("zmqpp/CMakeLists.txt", "# Build flags",
                '''# Build flags
set( IS_CONAN_BUILD       true    CACHE bool "Defines CONAN_BUILD" )
if (IS_CONAN_BUILD)
  include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
  conan_basic_setup()
endif()''')

    def build(self):
        cmake = CMake(self)
        opts = {"IS_CONAN_BUILD": "ON",
                "ZMQPP_BUILD_STATIC": "OFF",
                "ZMQPP_BUILD_SHARED": "ON",
                "ZMQPP_BUILD_CLIENT": "ON" if self.options.build_client else "OFF"}
        cmake.configure(defs=opts, source_dir="zmqpp", build_dir="./")
        cmake.build()

    def package(self):
        self.copy("*.hpp", dst="include/zmqpp", src="zmqpp/src/zmqpp")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False, symlinks=True)
        self.copy("*.so*", dst="lib", keep_path=False, symlinks=True)
        self.copy("*", dst="bin", src="bin", keep_path=False)
        self.copy("license*", dst="licenses", src="zmqpp", ignore_case=True, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["zmqpp"]
