# Qt MOC Generator
Integration of generation of Qt Meta-Object code using the Meta-Object Compiler (moc) in GN build system.

### Introduction
This repo contains a GN defintion file (`qt_generator.gni`)and the generation python script (`qt_moc_generator.py`).

### Requirements
* GN meta-build system ([more information](https://chromium.googlesource.com/chromium/src/tools/gn/))
* Qt Meta-Object Compiler ([info](http://doc.qt.io/qt-4.8/moc.html))

### Usage

Import the .gni file in the `BUILD.gn` where you need to generate Qt meta-object sources. 

```python
import("//project-root/{dir}/qt_generator.gni")
```

Create a built source_set, for example:

```python
qt_moc_generator("qt_sources") {
    sources = [
        "src/qt_header1.h",
        "src/qt_header2.h",
    ]
    include_dirs = [
        "/usr/include/qt5",
        "/usr/include/qt5/QtCore",
    ]
    moc_out_dir = "qt/generated_moc"
}
```

Then in your target library or executable, add the generated as part of the dependencies,

```python 
executable("awesome_exec") {
    sources = [
        "src/source1.cc",
        "src/source2.cc",
        "src/source3.cc",
        "src/main.cc"
    ]
    deps = [
        "//third_party/deps1",
        "//third_party/deps2",
        ":qt_sources"
    ]
    cflags = [
        "-Wno-error"
    ]
    libs = [
        "Qt5Core",
    ]
}
```

Afterwards, simply run `gn gen <folder>` and build, the scripts will automatically generate the required meta-object sources and object files and include in your project/library.

