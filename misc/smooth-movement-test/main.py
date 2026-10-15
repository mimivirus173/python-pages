import pygame as pg, asyncio, sys, time

pg.init()

if sys.platform == "emscripten":
    from js import window
    SCREEN_WIDTH, SCREEN_HEIGHT = int(window.innerWidth), int(window.innerHeight)
else:
    SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000
SPEED = 3
FRICTION = 0.9

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# player: float position and velocity
px, py = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
vx = vy = 0.0
SIZE = 50

if sys.platform == "emscripten":
    from pyodide.ffi import create_once_callable
    from js import requestAnimationFrame

    def next_frame():
        fut = asyncio.get_running_loop().create_future()
        requestAnimationFrame(create_once_callable(lambda t: fut.set_result(t)))
        return fut
else:
    async def next_frame():
        await asyncio.sleep(1 / 60)

async def main():
    global px, py, vx, vy
    last = time.perf_counter()

    run = True
    while run:
        now = time.perf_counter()
        f = min((now - last) * 60, 3)  # elapsed time in "60 FPS frames", capped
        last = now

        key = pg.key.get_pressed()
        left = key[pg.K_a] or key[pg.K_LEFT]
        right = key[pg.K_d] or key[pg.K_RIGHT]
        up = key[pg.K_w] or key[pg.K_UP]
        down = key[pg.K_s] or key[pg.K_DOWN]

        # same feel as before, scaled by elapsed time
        vx += (right - left) * SPEED * f
        vx *= FRICTION ** f
        vy += (down - up) * SPEED * f
        vy *= FRICTION ** f

        px += vx * f
        py += vy * f

        for event in pg.event.get():
            if event.type == pg.QUIT or key[pg.K_ESCAPE]:
                run = False

        screen.fill((0, 0, 0))
        pg.draw.rect(screen, (255, 255, 255), (round(px), round(py), SIZE, SIZE))
        pg.display.update()

        await next_frame()

    pg.quit()

if sys.platform != "emscripten":
    asyncio.run(main())