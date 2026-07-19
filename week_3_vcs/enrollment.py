def build_profile(name, **details):
    print("Student Name:", name)

    for key, value in details.items():
        print(f"{key}: {value}")
build_profile(
    "Sanskar",
    age=20,
    program="BScIT",
    semester=4,
    portfolio="https://github.com/sanskar",
    email="sanskardhakal69@gmail.com"
)