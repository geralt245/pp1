def vat(amount):
    vat = (23 / 100) * amount

    return (f"Amount : {amount} zł\nVAT 23% : {vat}")

print(vat(100532105.52346))