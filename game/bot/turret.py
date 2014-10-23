

aimAngle = 90
turretAngle = 0
turnAmount = 1

if aimAngle > turretAngle:
    difference = aimAngle - turretAngle
    if difference > 180:
        turnAmount = -turnAmount
else:
    difference = turretAngle - aimAngle
    if difference < 180:
        turnAmount = -turnAmount

turretAngle = (turretAngle + turnAmount) % 360





