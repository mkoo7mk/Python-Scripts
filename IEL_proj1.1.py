u1 = 130
u2 = 60
r1 = 380
r2 = 420
r3 = 330
r4 = 440
r5 = 450
r6 = 650
r7 = 410
r8 = 275


# u1 = 115
# u2 = 55
# r1 = 485
# r2 = 660
# r3 = 100
# r4 = 340
# r5 = 575
# r6 = 815
# r7 = 255
# r8 = 225


u12 = u1 + u2
r23 = r2 * r3 / (r2 + r3)

r68 = r6 + r8

# Trojuholnik na hviezdu
ra = (r23 * r4) / (r23 + r4 + r5)
rb = (r23 * r5) / (r23 + r4 + r5)
rc = (r5 * r4) / (r23 + r4 + r5)

print(f'Ra: {ra}, Rb: {rb}, Rc: {rc}')


rb68 = rb + r68
print('rb68: ', rb68)
rc7 = rc + r7
print('rc7: ', rc7)
ra1 = ra + r1
print('ra1: ', ra1)

rb68c7 = (rb68 * rc7) / (rb68 + rc7)
print('rb68c7: ', rb68c7)

rekv = ra1 + rb68c7

print('rekv', rekv)

i = u12 / rekv
print('i: ', i)
i1a = i
i68b7c = i
ur1a = i * ra1
print('ur1a: ', ur1a)
ur68bc7 = i * rb68c7
print('ur68bc7: ', ur68bc7)


ur1 = i * r1
print('ur1: ', ur1)
ura = i * ra
print('ura: ', ura)

irb = ur68bc7 / rb68
print('irb: ', irb)
urb = irb * rb
print('urb: ', urb)


irc7 = ur68bc7 / rc7
irb68 = ur68bc7 / rb68

print('irc7: ', irc7)
print('irb68: ', irb68)
irb = ur68bc7 / rb68
ir68 = ur68bc7 / rb68
ur68 = ir68 * r68
print('irb: ', irb)
print('ir68: ', ir68)
print('ur68', ur68)


irc = ur68bc7 / rc7
ir7 = ur68bc7 / rc7
urc = irc * rc
ur7 = ir7 * r7

ur4 = u12 - ur1 -ur7
ur23 = u12 - ur1 - ur68
ur5 = ur68 - ur7

print(f'Ur4 = {ur4}')
print(f'ur23 = {ur23}')
print(f'ur5 = {ur5}')

print(f'Ur7 = {ur7}')
print(f'urc = {urc}')
print(f'irc = {irc}')

i23 = ur23 / r23 
i4 = ur4 / r4
i5 = ur5 / r5
i68 = ur68 / r68
i7 = ur7 / r7

print(f'I23 = {i23}')
print(f'I4 = {i4}')
print(f'I5 = {i5}')
print(f'I68 = {i68}')
print(f'I7 = {i7}')

ir2 = (ur23 * r2) / (ur23 + r2)
ir3 = (ur23 * r3) / (ur23 + r3)
ur6 = ir68 * r6
ur8 = ir68 * r8

ur2 = i23 * r2
print('ur2: ', ur2)

print(f'Ir2 = {ir2}')
print(f'Ir3 = {ir3}')
print(f'Ur6 = {ur6}')
print(f'Ur8 = {ur8}')