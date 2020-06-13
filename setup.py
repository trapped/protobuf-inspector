import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="protobuf-inspector",
    version="0.1.0",
    author="Alba Mendez",
    author_email="me@alba.sh",
    description="Tool to reverse-engineer Protocol Buffers with unknown definition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mildsunrise/protobuf-inspector",
    packages=["protobuf_inspector", "protobuf_inspector.lib"],
    entry_points=dict(
        console_scripts=["protobuf-inspector = protobuf_inspector.main:main"]
    ),
    python_requires=">=3.6",
)
