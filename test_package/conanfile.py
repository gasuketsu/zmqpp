from conans import ConanFile, CMake
from os import getenv
from os import path


class ZmqppConanTest(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    username = getenv("CONAN_USERNAME", "gasuketsu")
    channel = getenv("CONAN_CHANNEL", "stable")
    requires = "zmqpp/4.1.2@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure(build_dir="./")
        cmake.build()

    def test(self):
        self.run(path.join("bin", "ConanZmqppTest"))
