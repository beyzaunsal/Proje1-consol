def cisimyüksekliksüre():
    t=int(input("Cismin yere indiği süre nedir?"))
    g=9.81
    def süre(t):
        return 0.5*g*t**2
    print(f"Yere düşme süresine göre, bu cisim {0.5*g*t**2} yükseklikten düşmüştür.")

    h=int(input("Cisim kaç metre yükseklikten bırakılmıştır?"))
    g=9.81
    def yükseklik(h):
        return h/0.5*g
    num_sqrt = h/0.5*g
    print(f"{h} m yükseklikten bırakılan cisim {num_sqrt} sürede yere düşmüştür.")
    input()