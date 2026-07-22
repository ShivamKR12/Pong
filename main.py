import pygame, sys, random, os


# The Block class is the most basic sprite in this project.
class Block(pygame.sprite.Sprite):
	def __init__(self, path, x_pos, y_pos):
		super().__init__()
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(center = (x_pos, y_pos))


# The Player class represents the paddle controlled by the user.
class Player(Block):
	def __init__(self, path, x_pos, y_pos, speed):
		super().__init__(path, x_pos, y_pos)
		self.speed = speed
		self.movement = 0
		# Track absolute touch targets for smooth mobile navigation
		self.touch_target_y = None 

	def screen_constrain(self, current_screen_height):
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= current_screen_height:
			self.rect.bottom = current_screen_height

	def update(self, ball_group, current_screen_height):
		# If we have an active touch target, step towards it
		if self.touch_target_y is not None:
			if abs(self.rect.centery - self.touch_target_y) > self.speed:
				if self.rect.centery < self.touch_target_y:
					self.rect.y += self.speed
				else:
					self.rect.y -= self.speed
		else:
			# Fallback to keyboard-driven delta movement
			self.rect.y += self.movement
			
		self.screen_constrain(current_screen_height)


# The Ball class handles physical interaction and the countdown timer state.
class Ball(Block):
	def __init__(self, path, x_pos, y_pos, speed_x, speed_y, paddles):
		super().__init__(path, x_pos, y_pos)
		self.speed_x = speed_x * random.choice((-1, 1))
		self.speed_y = speed_y * random.choice((-1, 1))
		self.paddles = paddles
		self.active = False
		self.score_time = 0

	def update(self, current_screen_width, current_screen_height):
		if self.active:
			self.rect.x += self.speed_x
			self.rect.y += self.speed_y
			self.collisions(current_screen_height)
		else:
			self.restart_counter(current_screen_width, current_screen_height)

	def collisions(self, current_screen_height):
		if self.rect.top <= 0 or self.rect.bottom >= current_screen_height:
			pygame.mixer.Sound.play(plob_sound)
			self.speed_y *= -1

		if pygame.sprite.spritecollide(self, self.paddles, False):
			pygame.mixer.Sound.play(plob_sound)
			collision_paddle = pygame.sprite.spritecollide(self, self.paddles, False)[0].rect

			if abs(self.rect.right - collision_paddle.left) < 10 and self.speed_x > 0:
				self.speed_x *= -1
			if abs(self.rect.left - collision_paddle.right) < 10 and self.speed_x < 0:
				self.speed_x *= -1
			if abs(self.rect.top - collision_paddle.bottom) < 10 and self.speed_y < 0:
				self.rect.top = collision_paddle.bottom
				self.speed_y *= -1
			if abs(self.rect.bottom - collision_paddle.top) < 10 and self.speed_y > 0:
				self.rect.bottom = collision_paddle.top
				self.speed_y *= -1

	def reset_ball(self, current_screen_width, current_screen_height):
		self.active = False
		self.speed_x *= random.choice((-1, 1))
		self.speed_y *= random.choice((-1, 1))
		self.score_time = pygame.time.get_ticks()
		self.rect.center = (current_screen_width / 2, current_screen_height / 2)
		pygame.mixer.Sound.play(score_sound)

	def restart_counter(self, current_screen_width, current_screen_height):
		current_time = pygame.time.get_ticks()
		countdown_number = 3

		if current_time - self.score_time <= 700:
			countdown_number = 3
		if 700 < current_time - self.score_time <= 1400:
			countdown_number = 2
		if 1400 < current_time - self.score_time <= 2100:
			countdown_number = 1
		if current_time - self.score_time >= 2100:
			self.active = True

		time_counter = basic_font.render(str(countdown_number), True, accent_color)
		time_counter_rect = time_counter.get_rect(center = (current_screen_width / 2, current_screen_height / 2 + 50))
		pygame.draw.rect(screen, bg_color, time_counter_rect)
		screen.blit(time_counter, time_counter_rect)


# The Opponent class represents the AI paddle.
class Opponent(Block):
	def __init__(self, path, x_pos, y_pos, speed):
		super().__init__(path, x_pos, y_pos)
		self.speed = speed

	def update(self, ball_group, current_screen_height):
		if self.rect.top < ball_group.sprite.rect.y:
			self.rect.y += self.speed
		if self.rect.bottom > ball_group.sprite.rect.y:
			self.rect.y -= self.speed
		self.constrain(current_screen_height)

	def constrain(self, current_screen_height):
		if self.rect.top <= 0: self.rect.top = 0
		if self.rect.bottom >= current_screen_height: self.rect.bottom = current_screen_height


# The GameManager class ties everything together.
class GameManager:
	def __init__(self, ball_group, paddle_group):
		self.player_score = 0
		self.opponent_score = 0
		self.ball_group = ball_group
		self.paddle_group = paddle_group

	def run_game(self, current_screen_width, current_screen_height):
		self.paddle_group.draw(screen)
		self.ball_group.draw(screen)

		# Pass dynamic screen boundaries down to update cycles
		self.paddle_group.update(self.ball_group, current_screen_height)
		self.ball_group.update(current_screen_width, current_screen_height)
		self.check_score(current_screen_width, current_screen_height)
		self.draw_score(current_screen_width, current_screen_height)

	def check_score(self, current_screen_width, current_screen_height):
		if self.ball_group.sprite.rect.right >= current_screen_width:
			self.opponent_score += 1
			self.ball_group.sprite.reset_ball(current_screen_width, current_screen_height)
		if self.ball_group.sprite.rect.left <= 0:
			self.player_score += 1
			self.ball_group.sprite.reset_ball(current_screen_width, current_screen_height)

	def draw_score(self, current_screen_width, current_screen_height):
		player_score = basic_font.render(str(self.player_score), True, accent_color)
		opponent_score = basic_font.render(str(self.opponent_score), True, accent_color)

		player_score_rect = player_score.get_rect(midleft = (current_screen_width / 2 + 40, current_screen_height / 2))
		opponent_score_rect = opponent_score.get_rect(midright = (current_screen_width / 2 - 40, current_screen_height / 2))

		screen.blit(player_score, player_score_rect)
		screen.blit(opponent_score, opponent_score_rect)


# Initialization and Window Setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

# Starting dimensions (can change dynamically now)
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

PATH = os.path.abspath(".") + "/"

bg_color = pygame.Color('#2F373F')
accent_color = (27, 35, 43)
basic_font = pygame.font.Font('freesansbold.ttf', 32)
plob_sound = pygame.mixer.Sound(PATH + "assets/pong.ogg")
score_sound = pygame.mixer.Sound(PATH + "assets/score.ogg")

# Initial layout positions
player = Player(PATH + 'assets/Paddle.png', screen_width - 20, screen_height / 2, 5)
opponent = Opponent(PATH + 'assets/Paddle.png', 20, screen_height / 2, 5)

paddle_group = pygame.sprite.Group()
paddle_group.add(player)
paddle_group.add(opponent)

ball = Ball(PATH + 'assets/Ball.png', screen_width / 2, screen_height / 2, 4, 4, paddle_group)
ball_sprite = pygame.sprite.GroupSingle()
ball_sprite.add(ball)

game_manager = GameManager(ball_sprite, paddle_group)

# Track active finger ID operating on the right side of the screen
active_finger_id = None

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_AC_BACK):
			pygame.quit()
			sys.exit()
			
		# HANDLE SCREEN RESIZING
		if event.type == pygame.VIDEORESIZE:
			screen_width, screen_height = event.w, event.h
			screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
			
			# Snap the elements immediately to their relative positions on resize
			player.rect.right = screen_width - 20
			opponent.rect.left = 20
			if not ball.active:
				ball.rect.center = (screen_width / 2, screen_height / 2)
				
		# Touch Controls
		if event.type == pygame.FINGERDOWN:
			if event.x > 0.5 and active_finger_id is None:
				active_finger_id = event.finger_id
				player.touch_target_y = event.y * screen_height

		if event.type == pygame.FINGERMOTION:
			if event.finger_id == active_finger_id:
				player.touch_target_y = event.y * screen_height

		if event.type == pygame.FINGERUP:
			if event.finger_id == active_finger_id:
				active_finger_id = None
				player.touch_target_y = None

	screen.fill(bg_color)
	
	# Render the middle strip line dynamically based on live width/height
	middle_strip = pygame.Rect(screen_width / 2 - 2, 0, 4, screen_height)
	pygame.draw.rect(screen, accent_color, middle_strip)

	# Run the game using the current resolution dimensions
	game_manager.run_game(screen_width, screen_height)

	pygame.display.flip()
	clock.tick(120)
