from bs4 import BeautifulSoup


replace_name_dict = {"Gabriel Finocchi" : "Gabe Finocchi",
                     "Paq Clifford" : "Anthony Clifford",
                     "Trevor Clements 704trev" : "Trevor Clements"}


def scrapeFile(file):
    ranks = []
    teams = []
    player_ones = []
    player_twos = []
    open_file = open(file, "r", encoding="utf8")
    soup = BeautifulSoup(str(open_file.readline()), 'lxml')
    for tag in soup.find_all("td", attrs={"class":"rank-column"}):
        if str(tag.contents[0]).find("gold") != -1:
            ranks.append(1)
        elif str(tag.contents[0]).find("silver") != -1:
            ranks.append(2)
        elif str(tag.contents[0]).find("bronze") != -1:
            ranks.append(3)
        else:
            ranks.append(int(tag.contents[0]))
    for tag in soup.find_all("div", attrs={"class":"team-name"}):
        teams.append(str(tag.contents[0]))
    for tag in soup.find_all("div", attrs={"class":"players"}):
        text = str(tag.contents[0])
        index = text.find(' and ')
        player_ones.append(cleanName(text[:index]))
        text = text[index:]
        text = text[1:]
        index = text.find(' ')
        player_twos.append(cleanName(text[index+1:]))
        text = text[index+1:]
    return ranks, [teams, player_ones, player_twos]


def cleanName(name : str):
    cleaned_name = ''
    name = name.replace("  ", " ")
    names = name.split(" ")
    for value in names:
        cleaned_name += f"{value[0].upper()}{value[1:].lower()} "
    cleaned_name = cleaned_name.strip(" ")
    if cleaned_name in replace_name_dict.keys():
        cleaned_name = replace_name_dict[cleaned_name]
    return cleaned_name
