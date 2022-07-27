import excel_reader as excel 
import selenium_flow as selenium
def main():
    sel = selenium.SeleniumReader("/Users/wiu/chromedriver", "https://www.greenfoot.org/home")
    nomes = excel.read('selenium-playground/__files/names.xlsx', 'Name')
    print("Total de itens para processar é: ", len(nomes), "...") 
    for name in nomes:
        print("processando nome ", name)
        sel.initCrawler(name)
    print("Fim de execução") 
main()