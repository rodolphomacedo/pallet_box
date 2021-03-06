# Access the browser: file:///home/user/Projects/pallet_box/paletes.html

# ------------------------------------------------------------
# *** Inputs to pallet_box ***
# Measured in millimeters 

# Input the pallet size
PALLET_WIDTH    = 1000      # PBR: 1000
PALLET_LENGTH   = 1200      # PBR: 1200

# Input the box size
BOX_WIDTH       = 245
BOX_LENGTH      = 95

# Loosen size
#   ATENTION: Allow the boxes to remain as few millimeters off the pallet
#       Default use: 0
LOOSEN = 0

# ------------------------------------------------------------
# *** Inputs the general setup ***
TEMPERATURE_INITIAL = 20.0
DECAY_INITIAL = 0.005
STEPS_INITIAL = 50

# Changes the efficiency accounting
#   False:= Num of boxs
#   True:=  Filled area
#       Default use: False
MODEL_EFFICIENCY = False

# standardize the pallet and boxs
#   True:= Resizes the pallet with box dimensions (Using M.D.C)
#   False:= Uses the measures of the standard pallet
#       Default use: False
STANDARDIZE = False

# Number of rounds
# Number of times the program will run from the initial configuration
#   Default use: 1
ROUNDS = 1

# Break with best box
#   For when the system reaches the desired number of boxes
#   Default -1 -> Do not Stop
BREAKINGBESTBOXS = -1


# ------------------------------------------------------------
# Measured in millimeters

# === Modelos de Teste ===
# Hello world - 15 caixas
#gridx = 400
#gridy = 200
#palX = 1000
#palY = 1200

# Ricieri - 21 caixas
#gridx = 345
#gridy = 160
#palX = 1000
#palY = 1200

# === Modelos Alimentacao ===
# Medidas Finni - 26 caixas
#gridx = 240
#gridy = 180
#palX = 1000
#palY = 1200

# === Modelos Racao Animal ======
# DogChow (Cx Verde) e CatChow (Cx Verde) - 48 caixas
#gridx = 95
#gridy = 245
#palX = 1000
#palY = 1200

# Friskies Purina (Cx Amarela) - 48 Caixas
#gridx = 95
#gridy = 245
#palX = 1000
#palY = 1200

# Sabor e Vida (Cx Verde Escura) - 30 Caixas
#gridx = 305
#gridy = 102
#palX = 1000
#palY = 1200

# Whiskas Petiscos (Papelao) - 16 Caixas
#gridx = 240
#gridy = 290
#palX = 1000
#palY = 1200

#Doguitos Purina (Cx Vermelha/Rosa) - 21 Caixas
#gridx = 125
#gridy = 385
#palX = 1000
#palY = 1200













