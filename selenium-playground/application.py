import excel_reader as excel 
import selenium_flow as selenium
import os 

def main():
    pathFolderFiles = os.getcwd() + "/python/selenium-playground/__files" 
    sel = selenium.SeleniumReader(pathFolderFiles + "/chromedriver/chromedriver_win32/chromedriver.exe", "https://www.greenfoot.org/home")
    nomes = excel.read(pathFolderFiles + "/names.xlsx", 'Name')
    print("Total de itens para processar é: ", len(nomes), "...") 
    for name in nomes:
        print("processando nome ", name)
        sel.initCrawler(name)
    print("Fim de execução") 
main()