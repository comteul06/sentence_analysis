import data_writer as dw

list = ["And in that light, I find deliberance.", "But hey, never say never.", "Smoke weed everyday."]

dw.set_snts(list)

for i in range(30):
    print(dw.get_snt())