from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="zogi", channel="stable")
    builder.add_common_builds(shared_option_name="blosc:shared")
    builder.run()
