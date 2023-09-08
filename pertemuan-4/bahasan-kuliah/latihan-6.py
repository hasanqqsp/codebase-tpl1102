huruf = input("Masukan sebuah huruf")

if len(huruf) > 1:
    print("Hanya 1 huruf")
else:
    if huruf in "aiueoAIUEO":
        print(f"Benar, {huruf} adalah huruf vokal")
    else:
        print(f"Salah, {huruf} bukan huruf vokal")
