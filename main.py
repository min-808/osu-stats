import sys
import time
import os
import requests

osuName = ""
correctCapitalization = ""

response = ""
parsedResponse = ""
bestResponse = ""
parsedbestReponse = ""
recentResponse = ""
parsedrecentResponse = ""

editAPI = False

def askforAPI():
    global editAPI
    os.system("cls")
    checkAPI = open("api.txt", "r")
    checking = checkAPI.read()
    if (checking == "") or (editAPI == True):
        print("Before you start using this application you must set an API key")
        print("Once set, we won't ask you again unless it's invalid!")
        apiCode = str(input("\nPaste in your API key, found at https://old.ppy.sh/p/api/\n").strip())
        api = open("api.txt", "w")
        api.write(apiCode)
        api.close()
        print("\nThank you!")
        time.sleep(1.5)
        askforName()
    else:
        print("API Key already filled in!")
        # time.sleep(1) This won't display, but if it skips to askforName() it means it was successful

def askforName():
    global response
    global parsedResponse
    global bestResponse
    global parsedbestResponse
    global recentResponse
    global parsedrecentReponse
    global osuName
    global correctCapitalization
    os.system("cls")
    apiKey = open("api.txt", "r")
    readapiKey = apiKey.read()
    apiKey.close()
    osuName = str(input("Hello! Input your osu! username\n").strip())
    response = requests.get("https://osu.ppy.sh/api/get_user?k=" + readapiKey + "&u=" + osuName + "&m=0")
    parsedResponse = response.json()
    if (parsedResponse == []) or (parsedResponse == {"error":"Please provide a valid API key."}):
        def foundError():
            global editAPI
            print("\n! Username or API key is invalid.\n")
            print("If you'd like to edit your API key, enter 'API'")
            print("If you'd like to enter a new username, enter to continue\n")
            fix = str(input("").strip())
            if fix == "":
                askforName()
            elif fix == "API":
                editAPI = True
                askforAPI()
            else:
                os.system("cls")
                print("That wasn't a valid option!")
                foundError()
        foundError()
            
    else:
        bestResponse = requests.get("https://osu.ppy.sh/api/get_user_best?k=" + readapiKey + "&u=" + osuName + "&m=0" + "&limit=1")
        parsedbestResponse = bestResponse.json()

        recentResponse = requests.get("https://osu.ppy.sh/api/get_user_recent?k=" + readapiKey + "&u=" + osuName + "&m=0" + "&limit=1")
        parsedrecentResponse = recentResponse.json()
    
        country = parsedResponse[0]["country"]
        correctCapitalization = parsedResponse[0]["username"]
        print("\n! Username validated")
        time.sleep(1)
        os.system("cls")
        def optionsList():
            global correctCapitalization
            print("Welcome", correctCapitalization + ", from " + country + "\n")
            print("-\n\n1. Ranks\n2. PP\n3. Level\n4. Accuracy\n5. Playcount & Playtime\n6. Score\n7. 300-100-50 Hit Ratio\n8. Grades\n9. Join Date\n0. Best & Recent Scores\n\nC. Change username\nI. Info\nE. Exit\n")
            chosenOption = str(input("-\n\nChoose an option: ").strip().capitalize())
            
            if chosenOption == "1":
                os.system("cls")
                globalRank = int(parsedResponse[0]["pp_rank"])
                countryRank = int(parsedResponse[0]["pp_country_rank"])
                print("Your current Global Rank is:  " + str("{:,}".format(globalRank)))
                print("Your current Country Rank is: " + str("{:,}".format(countryRank)))
                def askagainOptions():
                    askAgain = str(input("\n-\n\nEnter 'Y' to select another option, or enter 'N' to exit\n").strip().capitalize())
                    if askAgain == "Y":
                        print("\nLoading..")
                        time.sleep(1)
                        os.system("cls")
                        optionsList()
                    elif askAgain == "N":
                        print("\nThanks for using my app!")
                        time.sleep(1)
                        sys.exit()
                    else:
                        print("\nNot a valid option!")
                        askagainOptions()
                askagainOptions()
                
            elif chosenOption == "2":
                os.system("cls")
                PP = parsedResponse[0]["pp_raw"]
                print("Your current PP is: " + PP)
                def askagainOptions():
                    askAgain = str(input("\n-\n\nEnter 'Y' to select another option, or enter 'N' to exit\n").strip().capitalize())
                    if askAgain == "Y":
                        print("\nLoading..")
                        time.sleep(1)
                        os.system("cls")
                        optionsList()
                    elif askAgain == "N":
                        print("\nThanks for using my app!")
                        time.sleep(1)
                        sys.exit()
                    else:
                        print("\nNot a valid option!")
                        askagainOptions()
                askagainOptions()
                
            elif chosenOption == "3":
                os.system("cls")
                Level = parsedResponse[0]["level"]
                print("Your current Level is: " + Level)
                def askagainOptions():
                    askAgain = str(input("\n-\n\nEnter 'Y' to select another option, or enter 'N' to exit\n").strip().capitalize())
                    if askAgain == "Y":
                        print("\nLoading..")
                        time.sleep(1)
                        os.system("cls")
                        optionsList()
                    elif askAgain == "N":
                        print("\nThanks for using my app!")
                        time.sleep(1)
                        sys.exit()
                    else:
                        print("\nNot a valid option!")
                        askagainOptions()
                askagainOptions()

            elif chosenOption == "4":
                os.system("cls")
                Accuracy = str(round(float(parsedResponse[0]["accuracy"]), 2))
                print("Your current Accuracy is: " + Accuracy + "%")
                def askagainOptions():
                    askAgain = str(input("\n-\n\nEnter 'Y' to select another option, or enter 'N' to exit\n").strip().capitalize())
                    if askAgain == "Y":
                        print("\nLoading..")
                        time.sleep(1)
                        os.system("cls")
                        optionsList()
                    elif askAgain == "N":
                        print("\nThanks for using my app!")
                        time.sleep(1)
                        sys.exit()
                    else:
                        print("\nNot a valid option!")
                        askagainOptions()
                askagainOptions()

            elif chosenOption == "5":
                os.system("cls")
                Playcount = int(parsedResponse[0]["playcount"])
                Playtime = int(parsedResponse[0]["total_seconds_played"])

                convertDays = Playtime / 86400
                
                print("Your current Playcount is: " + str("{:,}".format(Playcount)))
                print("Your current Playtime is:  " + str(round(float(convertDays), 2)) + " Days")
                def askagainOptions():
                    askAgain = str(input("\n-\n\nEnter 'Y' to select another option, or enter 'N' to exit\n").strip().capitalize())
                    if askAgain == "Y":
                        print("\nLoading..")
                        time.sleep(1)
                        os.system("cls")
                        optionsList()
                    elif askAgain == "N":
                        print("\nThanks for using my app!")
                        time.sleep(1)
                        sys.exit()
                    else:
                        print("\nNot a valid option!")
                        askagainOptions()
                askagainOptions()

            elif chosenOption == "6":
                os.system("cls")
                rankedScore = int(parsedResponse[0]["ranked_score"])
                totalScore = int(parsedResponse[0]["total_score"])
                ratioScore = rankedScore / totalScore
                print("Your current Total Score is:  " + str("{:,}".format(totalScore)))
                print("Your current Ranked Score is: " + str("{:,}".format(rankedScore)))
                print("\nYour ranked score is " + str(round(float(ratioScore * 100), 2)) + "% of your total score")
                def askagainOptions():
                    askAgain = str(input("\n-\n\nEnter 'Y' to select another option, or enter 'N' to exit\n").strip().capitalize())
                    if askAgain == "Y":
                        print("\nLoading..")
                        time.sleep(1)
                        os.system("cls")
                        optionsList()
                    elif askAgain == "N":
                        print("\nThanks for using my app!")
                        time.sleep(1)
                        sys.exit()
                    else:
                        print("\nNot a valid option!")
                        askagainOptions()
                askagainOptions()

            elif chosenOption == "7":
                os.system("cls")
                ratio300 = int(parsedResponse[0]["count300"])
                ratio100 = int(parsedResponse[0]["count100"])
                ratio50 = int(parsedResponse[0]["count50"])

                percent300 = ratio300 / (ratio300 + ratio100 + ratio50)
                percent300 = " (" + str(round(float(percent300 * 100), 2)) + "%)"

                percent100 = ratio100 / (ratio300 + ratio100 + ratio50)
                percent100 = " (" + str(round(float(percent100 * 100), 2)) + "%)"

                percent50 = ratio50 / (ratio300 + ratio100 + ratio50)
                percent50 = " (" + str(round(float(percent50 * 100), 2)) + "%)"

                totalHits = ratio300 + ratio100 + ratio50
                
                print("300s hit: " + str("{:,}".format(ratio300)) + percent300)
                print("100s hit: " + str("{:,}".format(ratio100)) + percent100)
                print("50s hit:  " + str("{:,}".format(ratio50)) + percent50)
                print("\nTotal Hits: " + str("{:,}".format(totalHits)))
                
                def askagainOptions():
                    askAgain = str(input("\n-\n\nEnter 'Y' to select another option, or enter 'N' to exit\n").strip().capitalize())
                    if askAgain == "Y":
                        print("\nLoading..")
                        time.sleep(1)
                        os.system("cls")
                        optionsList()
                    elif askAgain == "N":
                        print("\nThanks for using my app!")
                        time.sleep(1)
                        sys.exit()
                    else:
                        print("\nNot a valid option!")
                        askagainOptions()
                askagainOptions()

            elif chosenOption == "8":
                os.system("cls")
                gradeSS = int(parsedResponse[0]["count_rank_ss"])
                gradeSSH = int(parsedResponse[0]["count_rank_ssh"])
                gradeS = int(parsedResponse[0]["count_rank_s"])
                gradeSH = int(parsedResponse[0]["count_rank_sh"])
                gradeA = int(parsedResponse[0]["count_rank_a"])

                totalGrades = gradeSS + gradeSSH + gradeS + gradeSH + gradeA
                
                gradeSSRatio = gradeSS / totalGrades
                gradeSSRatio = str(round(float(gradeSSRatio * 100), 2))
                gradeSSHRatio = gradeSSH / totalGrades
                gradeSSHRatio = str(round(float(gradeSSHRatio * 100), 2))
                gradeSRatio = gradeS / totalGrades
                gradeSRatio = str(round(float(gradeSRatio * 100), 2))
                gradeSHRatio = gradeSH / totalGrades
                gradeSHRatio = str(round(float(gradeSHRatio * 100), 2))
                gradeARatio = gradeA / totalGrades
                gradeARatio = str(round(float(gradeARatio * 100), 2))

                print("Hidden SS's: " + str("{:,}".format(gradeSSH)) + " (" + str(gradeSSHRatio) + "%)")
                print("Hidden S's:  " + str("{:,}".format(gradeSH)) + " (" + str(gradeSHRatio) + "%)" + "\n")
                print("SS's: " + str("{:,}".format(gradeSS)) + " (" + str(gradeSSRatio) + "%)")
                print("S's:  " + str("{:,}".format(gradeS)) + " (" + str(gradeSRatio) + "%)" + "\n")
                print("A's: " + str("{:,}".format(gradeA)) + " (" + str(gradeARatio) + "%)" + "\n")

                print("Total clears: " + str("{:,}".format(totalGrades)))
                
                def askagainOptions():
                    askAgain = str(input("\n-\n\nEnter 'Y' to select another option, or enter 'N' to exit\n").strip().capitalize())
                    if askAgain == "Y":
                        print("\nLoading..")
                        time.sleep(1)
                        os.system("cls")
                        optionsList()
                    elif askAgain == "N":
                        print("\nThanks for using my app!")
                        time.sleep(1)
                        sys.exit()
                    else:
                        print("\nNot a valid option!")
                        askagainOptions()
                askagainOptions()

            elif chosenOption == "9":
                os.system("cls")
                joinDate = str(parsedResponse[0]["join_date"])
                print("You joined osu! on: " + joinDate[0:10] + " at " + joinDate[11:20] + " (UTC)")
                
                def askagainOptions():
                    askAgain = str(input("\n-\n\nEnter 'Y' to select another option, or enter 'N' to exit\n").strip().capitalize())
                    if askAgain == "Y":
                        print("\nLoading..")
                        time.sleep(1)
                        os.system("cls")
                        optionsList()
                    elif askAgain == "N":
                        print("\nThanks for using my app!")
                        time.sleep(1)
                        sys.exit()
                    else:
                        print("\nNot a valid option!")
                        askagainOptions()
                askagainOptions()

            elif chosenOption == "0":
                os.system("cls")
                bestbeatmapID = parsedbestResponse[0]["beatmap_id"]
                bestbeatmapResponse = requests.get("https://osu.ppy.sh/api/get_beatmaps?k=" + readapiKey + "&b=" + bestbeatmapID + "&m=0&limit=1")
                parsedbestbeatmapResponse = bestbeatmapResponse.json()

                recentbeatmapID = parsedrecentResponse[0]["beatmap_id"]
                recentbeatmapResponse = requests.get("https://osu.ppy.sh/api/get_beatmaps?k=" + readapiKey + "&b=" + recentbeatmapID + "&m=0&limit=1")
                parsedrecentbeatmapResponse = recentbeatmapResponse.json()

                # Best beatmap API grabbing
                bestbeatmapArtist = parsedbestbeatmapResponse[0]["artist_unicode"]
                bestbeatmapName = parsedbestbeatmapResponse[0]["title_unicode"]
                bestbeatmapDiff = parsedbestbeatmapResponse[0]["version"]
                bestbeatmapPP = parsedbestResponse[0]["pp"]
                bestbeatmapRank = parsedbestResponse[0]["rank"]
                bestbeatmapCreator = parsedbestbeatmapResponse[0]["creator"]
                bestbeatmapDate = parsedbestResponse[0]["date"]
                # Best ends here

                # Recent beatmap API grabbing
                recentbeatmapArtist = parsedrecentbeatmapResponse[0]["artist_unicode"]
                recentbeatmapName = parsedrecentbeatmapResponse[0]["title_unicode"]
                recentbeatmapDiff = parsedrecentbeatmapResponse[0]["version"]
                recentbeatmapRank = parsedrecentResponse[0]["rank"]
                recentbeatmapCreator = parsedrecentbeatmapResponse[0]["creator"]
                recentbeatmapDate = parsedrecentResponse[0]["date"]
                # Recent ends here

                print("Your best osu! score is on:\n")
                print(bestbeatmapArtist + " - " + bestbeatmapName + " [" + bestbeatmapDiff + "] (" + bestbeatmapCreator + ")")
                print(bestbeatmapRank + " Rank | " + bestbeatmapPP + " pp")
                print("Achieved on " + bestbeatmapDate[0:10] + " at " + bestbeatmapDate[11:20] + " (UTC)")

                print("\n")

                print("Your most recent osu! score is on:\n")
                print(recentbeatmapArtist + " - " + recentbeatmapName + " [" + recentbeatmapDiff + "] (" + recentbeatmapCreator + ")")
                print(recentbeatmapRank + " Rank")
                print("Achieved on " + recentbeatmapDate[0:10] + " at " + recentbeatmapDate[11:20] + " (UTC)")
                
                def askagainOptions():
                    askAgain = str(input("\n-\n\nEnter 'Y' to select another option, or enter 'N' to exit\n").strip().capitalize())
                    if askAgain == "Y":
                        print("\nLoading..")
                        time.sleep(1)
                        os.system("cls")
                        optionsList()
                    elif askAgain == "N":
                        print("\nThanks for using my app!")
                        time.sleep(1)
                        sys.exit()
                    else:
                        print("\nNot a valid option!")
                        askagainOptions()
                askagainOptions()

            elif chosenOption == "C":
                os.system("cls")
                askforName()

            elif chosenOption == "I":
                os.system("cls")
                print("osu!Stats made by Min\n")
                print("This is pretty much the osu! website on a console window lol")
                print("It's kinda useless but it was fun to make + I learned about APIs")
                print("\nI used osu!api v1 and Python's requests library")

                def askagainOptions():
                    askAgain = str(input("\n-\n\nEnter 'Y' to select another option, or enter 'N' to exit\n").strip().capitalize())
                    if askAgain == "Y":
                        print("\nLoading..")
                        time.sleep(1)
                        os.system("cls")
                        optionsList()
                    elif askAgain == "N":
                        print("\nThanks for using my app!")
                        time.sleep(1)
                        sys.exit()
                    else:
                        print("\nNot a valid option!")
                        askagainOptions()
                askagainOptions()

            elif chosenOption == "E":
                print("\nThanks for using my app!")
                time.sleep(1)
                sys.exit()

            elif chosenOption == "Debug1":
                os.system("cls")
                print(parsedResponse)
                def askagainOptions():
                    askAgain = str(input("\n-\n\nEnter 'Y' to select another option, or enter 'N' to exit\n").strip().capitalize())
                    if askAgain == "Y":
                        print("\nLoading..")
                        time.sleep(1)
                        os.system("cls")
                        optionsList()
                    elif askAgain == "N":
                        print("\nThanks for using my app!")
                        time.sleep(1)
                        sys.exit()
                    else:
                        print("\nNot a valid option!")
                        askagainOptions()
                askagainOptions()

            elif chosenOption == "Debug2":
                os.system("cls")
                print(parsedbestResponse)
                def askagainOptions():
                    askAgain = str(input("\n-\n\nEnter 'Y' to select another option, or enter 'N' to exit\n").strip().capitalize())
                    if askAgain == "Y":
                        print("\nLoading..")
                        time.sleep(1)
                        os.system("cls")
                        optionsList()
                    elif askAgain == "N":
                        print("\nThanks for using my app!")
                        time.sleep(1)
                        sys.exit()
                    else:
                        print("\nNot a valid option!")
                        askagainOptions()
                askagainOptions()

            elif chosenOption == "Debug3":
                os.system("cls")
                print(parsedrecentResponse)
                def askagainOptions():
                    askAgain = str(input("\n-\n\nEnter 'Y' to select another option, or enter 'N' to exit\n").strip().capitalize())
                    if askAgain == "Y":
                        print("\nLoading..")
                        time.sleep(1)
                        os.system("cls")
                        optionsList()
                    elif askAgain == "N":
                        print("\nThanks for using my app!")
                        time.sleep(1)
                        sys.exit()
                    else:
                        print("\nNot a valid option!")
                        askagainOptions()
                askagainOptions()
                
            else:
                print("\nThat wasn't a valid option!")
                print("Asking again..")
                time.sleep(1.5)
                os.system("cls")
                optionsList()
                
        optionsList()
        print("Resetting..")
        time.sleep(1.5)
        os.system("cls")
        askforName()

askforAPI()
askforName()
