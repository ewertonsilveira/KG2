

########
# GAME SETTINGS
###
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
GRAVITY = 0.75
TILE_SIZE = 40

 
########
# SHOTTING SETTINGS
###
GROUND = int(SCREEN_HEIGHT * 0.8)
COOLDOWN_PERIOD = 100


# Soldiers settings
SOLDIER_BASE_HEALTH = 120
SOLDIER_INITIAL_BULLETS = 100
SOLDIER_INITIAL_GRENADES = 3000

# Enemy settings
ENEMY_BASE_HEALTH = 50
ENEMY_BULLET_HEALTH_DAMAGE = 10
ENEMY_INITIAL_BULLETS = 200 * 100
ENEMY_INITIAL_GRENADES = 0


# Bullets settings
BULLET_SPEED = 7
SHOOT_COOLDOWN_TIMER = 10

# Grenade settings
GRENADE_SPEED = 7
GRENADE_TIMER = 100
GRENADE_COOLDOWN_TIMER = 10
GRENADE_HEALTH_DAMAGE = 30


# Grenade explosion
GRENADE_EXPLOSION_SCALE = 0.7