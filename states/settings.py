

########
# GAME SETTINGS
###
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
SCROLL_THRESHOLD = 200
GRAVITY = 0.75
ROWS = 16
COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 21

########
# SHOTTING SETTINGS
###
GROUND = int(SCREEN_HEIGHT * 0.8)
COOLDOWN_PERIOD = 100
PLAYERS_SCALE = 2.3

# Soldiers settings
SOLDIER_BASE_HEALTH = 300
SOLDIER_INITIAL_BULLETS = 60
SOLDIER_INITIAL_GRENADES = 15
SOLDIER_JUMP_POWER = -TILE_SIZE * 0.25


# Enemy settings
ENEMY_BASE_HEALTH = 70
ENEMY_BULLET_HEALTH_DAMAGE = 10
ENEMY_INITIAL_BULLETS = 25
ENEMY_INITIAL_GRENADES = 0
ENEMY_RUN_SPEED = 2
ENEMY_VISION_RANGE = 250

# Bullets settings
BULLET_SPEED = 7
SHOOT_COOLDOWN_TIMER = 10
BULLETS_SCALE = 1.8

# Grenade settings
GRENADE_SPEED = 7
GRENADE_TIMER = 100
GRENADE_COOLDOWN_TIMER = 10
GRENADE_HEALTH_DAMAGE = 35
GRENADE_SCALE = 1.5

# Grenade explosion
GRENADE_EXPLOSION_SCALE = 0.7

# Item Box 
ITEM_BOX_HEALTH = 25
ITEM_BOX_AMMO = 15
ITEM_BOX_GRENADE = 5