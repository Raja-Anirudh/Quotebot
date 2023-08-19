
# coding: utf-8

# In[1]:


#This only need to be runned in an offline python compiler. Ex:VSC, Pycharm, Spyder, python IDLEetc.

print("Hi I am quotebot")
print("I am a chatbot created to try to change your mood")
print("1.Inspirational Quotes")
print("2.Motivational Quotes")
print("3.Positive Vibes")
print("4.Happy Quotes")
print("5.Sad Quotes")
print("6.Angry Quotes")

while True:
    choice = input("Enter choice 1/2/3/4/5/6 to select your mood and I will try to change your mood: ")

    if choice in ('1', '2', '3', '4', '5', '6'):


        if choice == '1':
            print("Nothing is impossible. The word itself says 'I'm possible! - Audrey Hepburn")
            print("Keep your face always toward the sunshine, and shadows will fall behind you. - Walt Whitman")

            choice11 = input("Do you want to read some more yes/no: ")
            if choice11 == 'yes':
                print("It always seems impossible until it's done. - Nelson Mandela ")
                print("Success is a journey not a destination. - Ben Sweetland")
            else:
                if choice11 == 'no':
                    user1_choice11 = input("How are you feeling after reading the quotes good/bad?: ")
                    if user1_choice11 == 'good':
                        print("Thank you for your feedback! Meet you again next time.")
                        break
                    else:
                        if user1_choice11 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo, Meet you again next time.")
                            break
                else:
                    print("It's a typo, Meet you again next time.")
                    break

            choice12 = input("Do you want to read some more yes/no: ")
            if choice12 == 'yes':
                print("If you cannot do great things, do small things in a great way. - Napoleon Hill")
                print("If opportunity doesn't knock, build a door. - Milton Berle")

                user1_choice12 = input("How are you feeling after reading the quotes good/bad?: ")
                if user1_choice12 == 'good':
                    print("Thank you for your feedback! Meet you again next time.")
                    break
                else:
                    if user1_choice12 == 'bad':
                        print("Sorry for the inconvenience. Meet you again next time.")
                        break
                    else:
                        print("It's a typo, Meet you again next time.")
                        break
            else:
                if choice12 == 'no':
                    user1_choice13 = input("How are you feeling after reading the quotes good/bad?: ")
                    if user1_choice13 == 'good':
                        print("Thank you for your feedback! Meet you again next time.")
                        break
                    else:
                        if user1_choice13 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo, Meet you again next time.")
                            break


        if choice == '2':
            print("Learn as if you will live forever, live like you will die tomorrow. - Mahatma Gandhi")
            print("Success is not final; failure is not fatal: It is the courage to continue that counts. - Winston S. Churchill")

            choice21 = input("Do you want to read some more yes/no: ")
            if choice21 == 'yes':
                print("Success usually comes to those who are too busy looking for it. - Henry David Thoreau")
                print("I never dreamed about success. I worked for it. - Estée Lauder")
            else:
                if choice21 == 'no':
                    user2_choice21 = input("How are you feeling after reading the quotes good/bad?: ")
                    if user2_choice21 == 'good':
                        print("Thank you for your feedback! Meet you again next time.")
                        break
                    else:
                        if user2_choice21 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo, Meet you again next time.")
                            break
                else:
                    print("It's a typo, Meet you again next time.")
                    break

            choice22 = input("Do you want to read some more yes/no: ")
            if choice22 == 'yes':
                print("Don’t let yesterday take up too much of today. - Will Rogers")
                print("If you are working on something that you really care about, you don’t have to be pushed. The vision pulls you. - Steve Jobs")

                user2_choice22 = input("How are you feeling after reading the quotes good/bad?: ")
                if user2_choice22 == 'good':
                    print("Thank you for your feedback! Meet you again next time.")
                    break
                else:
                    if user2_choice22 == 'bad':
                        print("Sorry for the inconvenience. Meet you again next time.")
                        break
                    else:
                        print("It's a typo, Meet you again next time.")
                        break
            else:
                if choice22 == 'no':
                    user2_choice23 = input("How are you feeling after reading the quotes good/bad?: ")
                    if user2_choice23 == 'good':
                        print("Thank you for your feedback! Meet you again next time.")
                        break
                    else:
                        if user2_choice23 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo, Meet you again next time.")
                            break


        if choice == '3':
            print("Vibe high and the magic around you will unfold. - Akilnathan Logeswaran")
            print("Wherever you go, no matter what the weather, always bring your own sunshine. - Anthony J. Dangelo")

            choice31 = input("Do you want to read some more yes/no:")
            if choice31 == 'yes':
                print("Happiness is not something ready-made. It comes from your own actions. - Dalai Lama")
                print("You came to RADIATE the fullness of who you are. - Abraham Hicks")
            else:
                if choice31 == 'no':
                    user3_choice31 = input("How are you feeling after reading the quotes good/bad?: ")
                    if user3_choice31 == 'good':
                        print("Thank you for your feedback! Meet you again next time.")
                        break
                    else:
                        if user3_choice31 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo, Meet you again next time.")
                            break
                else:
                    print("It's a typo, Meet you again next time.")
                    break

            choice32 = input("Do you want to read some more yes/no: ")
            if choice32 == 'yes':
                print("Let the Good vibe Sunday well spent to bring us a week of content. - Napz Cherub Pellazo")
                print("People say nothing is impossible, but I do nothing every day. - A.A Milne")

                user3_choice32 = input("How are you feeling after reading the quotes good/bad?: ")
                if user3_choice32 == 'good':
                    print("Thank you for your feedback! Meet you again next time.")
                    break
                else:
                    if user3_choice32 == 'bad':
                        print("Sorry for the inconvenience. Meet you again next time.")
                        break
                    else:
                        print("It's a typo, Meet you again next time.")
                        break
            else:
                if choice32 == 'no':
                    user3_choice33 = input("How are you feeling after reading the quotes good/bad?: ")
                    if user3_choice33 == 'good':
                        print("Thank you for your feedback! Meet you again next time.")
                        break
                    else:
                        if user3_choice33 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo, Meet you again next time.")
                            break


        if choice == '4':
            print("The most important thing is to enjoy your life – to be happy. It’s all that matters. - Audrey Hepburn")
            print("Never regret anything that made you smile. - Mark Twain")

            choice41 = input("Do you want to read some more yes/no: ")
            if choice41 == 'yes':
                print("Happiness is the best makeup. - Drew Barrymore")
                print("If you want to be happy, be. - Leo Tolstoy")
            else:
                if choice41 == 'no':
                    user4_choice41 = input("How are you feeling after reading the quotes good/bad?: ")
                    if user4_choice41 == 'good':
                        print("Thank you for your feedback! Meet you again next time.")
                        break
                    else:
                        if user4_choice41 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo, Meet you again next time.")
                            break
                else:
                    print("It's a typo, Meet you again next time.")
                    break


            choice42 = input("Do you want to read some more yes/no: ")
            if choice42 == 'yes':
                print("Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi")
                print("There is no path to happiness. Happiness is the path. - Buddha")

                user4_choice42 = input("How are you feeling after reading the quotes good/bad?: ")
                if user4_choice42 == 'good':
                    print("Thank you for your feedback! Meet you again next time.")
                    break
                else:
                    if user4_choice42 == 'bad':
                        print("Sorry for the inconvenience. Meet you again next time.")
                        break
                    else:
                        print("It's a typo, Meet you again next time.")
                        break
            else:
                if choice42 == 'no':
                    user4_choice43 = input("How are you feeling after reading the quotes good/bad?: ")
                    if user4_choice43 == 'good':
                        print("Thank you for your feedback! Meet you again next time.")
                        break
                    else:
                        if user4_choice43 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo, Meet you again next time.")
                            break


        if choice == '5':
            print("First, accept sadness. Realize that without losing, winning isn’t so great. - Alyssa Milano")
            print("Every life has a measure of sorrow, and sometimes this is what awakens us. - Steven Tyler")

            choice51 = input("Do you want to read some more yes/no: ")
            if choice51 == 'yes':
                print("Behind every sweet smile, there is a bitter sadness that no one can ever see and feel. - Tupac Shakur")
                print("Sadness is also a kind of defense. - Ivo Andrich")
            else:
                if choice51 == 'no':
                    user5_choice51 = input("How are you feeling after reading the quotes good/bad?: ")
                    if user5_choice51 == 'good':
                        print("Thank you for your feedback! Meet you again next time.")
                        break
                    else:
                        if user5_choice51 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo, Meet you again next time.")
                            break
                else:
                    print("It's a typo, Meet you again next time.")
                    break

            choice52 = input("Do you want to read some more yes/no: ")

            if choice52 == 'yes':
                print("Don’t grieve. Anything you lose comes round in another form. - Rumi")
                print("You know, a heart can be broken, but it keeps on beating, just the same. - Fannie Flagg")

                user5_choice52 = input("How are you feeling after reading the quotes good/bad?: ")
                if user5_choice52 == 'good':
                    print("Thank you for your feedback! Meet you again next time.")
                    break
                else:
                    if user5_choice52 == 'bad':
                        print("Sorry for the inconvenience. Meet you again next time.")
                        break
                    else:
                        print("It's a typo, Meet you again next time.")
                        break
            else:
                if choice52 == 'no':
                    user5_choice53 = input("How are you feeling after reading the quotes good/bad?: ")
                    if user5_choice53 == 'good':
                        print("Thank you for your feedback! Meet you again next time.")
                        break
                    else:
                        if user5_choice53 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo, Meet you again next time.")
                            break


        if choice == '6':
            print("Don't waste you time in anger, regrets, worries and grudges. Life is too short to be unhappy. - Roy T.Bennett")
            print("To be angry is to let others’ mistakes punish yourself. - Buddha")

            choice61 = input("Do you want to read some more yes/no: ")
            if choice61 == 'yes':
                print("Anger blows out the lamp of the mind. - Robert G. Ingersoll")
                print("Whatever is begun in anger, ends in shame. - Benjamin Franklin")
            else:
                if choice61 == 'no':
                    user6_choice61 = input("How are you feeling after reading the quotes good/bad?: ")
                    if user6_choice61 == 'good':
                        print("Thank you for your feedback! Meet you again next time.")
                        break
                    else:
                        if user6_choice61 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo, Meet you again next time.")
                            break
                else:
                    print("It's a typo, Meet you again next time.")
                    break

            choice62 = input("Do you want to read some more yes/no: ")
            if choice62 == 'yes':
                print("A quick temper will make a fool of you soon enough. - Bruce Lee")
                print("Anger at oneself is a destructive thing. - Qui-Gon Jinn")

                user6_choice62 = input("How are you feeling after reading the quotes good/bad?: ")
                if user6_choice62 == 'good':
                    print("Thank you for your feedback! Meet you again next time.")
                    break
                else:
                    if user6_choice62 == 'bad':
                        print("Sorry for the inconvenience. Meet you again next time.")
                        break
                    else:
                        print("It's a typo, Meet you again next time.")
                        break
            else:
                if choice62 == 'no':
                    user6_choice63 = input("How are you feeling after reading the quotes good/bad?: ")
                    if user6_choice63 == 'good':
                        print("Thank you for your feedback! Meet you again next time.")
                        break
                    else:
                        if user6_choice63 == 'bad':
                            print("Sorry for the inconvenience. Meet you again next time.")
                            break
                        else:
                            print("It's a typo, Meet you again next time.")
                            break
                        

