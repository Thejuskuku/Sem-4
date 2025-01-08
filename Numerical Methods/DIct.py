
human1={"name":"jeevandas","occupation":"software engineer","age":20}
human2={"name":"JD","occupation":"pilot","age":28}

ls=[human1,human2]
for i in ls:
    print(i)

    s=input(f"enter salary of {i["name"]}")

    i["salary"]=s

    print(i["name"])
    print(i)

human2.popitem()

print(human2)