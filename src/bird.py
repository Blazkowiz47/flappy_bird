from utils import *


class Bird:
    IMGS = BIRD_IMAGES
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.image_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1
        # Calculate distance travelled (d) in one tick count
        d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2
        # If d travelled is >= 16 limit d to 16
        # i.e. bird has achieved terminal velocity
        if d >= 16:
            d = 16
        # If d is negative, i.e. bird is moving upwards,
        # increase d only little. sort of gives thrust effect
        if d < 0:
            d -= 2
        # update y co-ordinate of bird
        self.y = self.y + d
        # if bird is moving upward, tilt it anticlockwise
        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        # if bird is moving downward, tilt it clockwise
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.image_count += 1
        # ANIMATION_TIME = 5
        # So, till ims_count < 5 it will render wings down image
        # then, till ims_count < 10 it will render wings levelled image
        # then, till ims_count < 15 it will render wings up image
        # then, till ims_count < 20 it will render wings levelled image
        # then, it will reset the animation
        # in case of nose-diving, the image is always of levelled wings
        if self.image_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.image_count < self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.image_count < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.image_count < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.image_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.image_count = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.image_count = self.ANIMATION_TIME * 2
        # Rotate image
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(
            center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
