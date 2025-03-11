import pyjokes

def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)
    
if __name__=="__main__":
    lang = input("Choissisez une langue (en, de, es , it, gl) : ")
    tell_joke()