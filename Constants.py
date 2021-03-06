from cdecimal import Decimal

N_OF_RELEASED_MOLECULES       = Decimal('10000000')
DIFFUSION_CONSTANT            = Decimal('0.0000097')
TAU                           = Decimal('8')            # typically 1 - 10s
RELAYING_THRESHOLD            = Decimal('0.000000008')
CHEMOTAXIS_THRESHOLD          = Decimal('0.000000001')
RELAYING_DELAY                = 15   # s
RELAYING_REFRACTORY_PERIOD    = 300  # 120 - 600s
CHEMOTAXIS_REFRACTORY_PERIOD  = 100  # s
CHEMOTAXIS_STEP               = 20   # 20 nm over 100s
RANDOM_MOTION_SPEED           = 5    # 5nm/min
RADIUS_SCALE                  = 1e3
INFLUENCE_RADIUS              = 0.280
INFLUENCE_TIME                = 180
TIME_FRAME                    = 5
REFRACTION_TIME               = 300
RANDOM_MOTION_STEP            = 15
