# DD Pygame Project

This small project demonstrates a minimal Pygame application.

What I changed

- Fixed an incorrect import in `src/main.py`: replaced `from pygame import pygame` with `import pygame`.
- Added a simple `if __name__ == "__main__"` runner so the file can be executed directly.

Notes and tips

- The runtime showed this warning:

  Your system is avx2 capable but pygame was not built with support for it. The performance of some blits could be adversely affected. Consider enabling compile time detection with environment variables like `PYGAME_DETECT_AVX2=1` if you are compiling without cross compilation.

  This is only relevant if you compile pygame from source; it does not affect correctness. If you rely on maximum blit performance and you build pygame yourself, set the environment variable when building.

- To run:

```bash
python3 src/main.py
```

If you want, I can also add a small automated import test or a unit test that ensures Pygame can be imported without raising ImportError.