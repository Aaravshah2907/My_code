# NOTES ON manim 

## Running a file 
code used is:
```commandline
manim -pql file.py classname
```
-p  : play the file after animation is rendered </br>
-f  : Open the file location instead of playing </br>
--format gif : To get a gif file instead of mp4
-qm : medium quality (1280x720 30FPS) </br>
-qp : 2K ((2560x1440 60FPS))</br>
-qk : 4k quality (3840x2160 60FPS)</br>
-ql : low quality (480p 15FPS) </br>
-qh : high quality (1920x1080 60FPS)

## Creating Sections:
In the code use:
```python
def construct(self):
    # play the first animations...
    # you don't need a section in the very beginning as it gets created automatically
    self.next_section()
    # play more animations...
    self.next_section("this is an optional name that doesn't have to be unique")
    # play even more animations...
    self.next_section("this is a section without any animations, it will be removed")
```
To save the individual sections as well 
```commandline
manim --save_sections scene.py
```

## Arrow
https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow
