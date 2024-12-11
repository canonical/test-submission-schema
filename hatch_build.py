from hatchling.builders.hooks.plugin.interface import BuildHookInterface

class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        """Hook that runs at the start of the build process."""
        print("Initializing custom build process...")
        print(f"Building version: {version}")

    def finalize(self, version, build_data, artifact):
        """Hook that runs at the end of the build process."""
        print("Finalizing custom build process...")
        print("Build completed successfully!")

    def clean(self, version, build_data):
        """Hook that runs during the clean process."""

    def update_metadata(self, metadata):
        """Dynamically update metadata."""
