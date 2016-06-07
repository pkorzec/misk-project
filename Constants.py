from decimal import Decimal

n_of_molecules_released       = Decimal('10000000')
diffusion_constant            = Decimal('0.0000097')
tau                           = Decimal('5')            # typically 1 - 10s
relaying_threshold            = Decimal('0.000000008')
chemotaxis_threshold          = Decimal('0.000000001')
relaying_delay                = 15   # s
relaying_refractory_period    = 300  # 120 - 600s
chemotaxis_refractory_period  = 100  # s
chemotaxis_step               = 20   # 20 nm over 100s
random_motion_speed           = 5    # 5nm/min
