#Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines() #나중에 반복문을 돌리기 위해서 readlines()를 사용하여 배열형태로 받음.

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read() #텍스트 파일의 내용을 한 번에 읽어들임.

    for name in names:
        new_letter = letter_contents.replace("[name]", name.strip()) # replace를 한 형태를 return함.

        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as letter:
            letter.write(new_letter) #파일을 열고, 수정된 내용을 기재함.




