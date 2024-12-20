
from utils.dbhandler import DataBaseManager
from utils.plotmaker import PlotMaker,MapMaker

class Answerer:
    def __init__(self) -> None:
        self.db_urls = {
        'ubereats': 'sqlite:///databases/ubereats.db',
        'deliveroo': 'sqlite:///databases/deliveroo.db',
        'takeaway': 'sqlite:///databases/takeaway.db'
        }
        self.file_paths_kaps = {
            'ubereats': 'vizualizations_data/kapsalons_data/kapsalons_ubereats.csv', 
            'takeaway': 'vizualizations_data/kapsalons_data/kapsalons_takeaway.csv', 
            'deliveroo': 'vizualizations_data/kapsalons_data/kapsalons_deliveroo.csv'
            }
        self.file_paths = {
            'ubereats': 'vizualizations_data/ubereats_data.csv', 
            'takeaway': 'vizualizations_data/takeaway_data.csv', 
            'deliveroo': 'vizualizations_data/deliveroo_data.csv'}
        self.border_path = 'vizualizations_data/belgium-with-regions_.geojson'
        self.manager = DataBaseManager(self.db_urls)


    def answer_quest_1(self):
        print("What is the price distribution of menu items?")
        df = self.manager.create_prices_df_for_all_db()
        ploter = PlotMaker(df,'Takeawy')
        ploter.price_distribution()

    def answer_quest_2(self):
        print('What is the distribution of restaurants per location')
        self.manager.create_prices_df_for_all_db()
        ploter = MapMaker(file_paths=self.file_paths)
        ploter.create_combined_map(self.border_path)
        ploter.create_individual_maps(self.border_path)

    def answer_quest_3(self):
        print('Which are the top 10 pizza restaurants by rating?')
        df_uber = self.manager.get_top10_Pizza_restaurants('ubereats')
        df_takeaway = self.manager.get_top10_Pizza_restaurants('takeaway')
        df_deliveroo = self.manager.get_top10_Pizza_restaurants('deliveroo')
        ploter = PlotMaker(df_uber,'UberEats')
        ploter.create_top_ten_pizza_plot()
        ploter.change_df(df_takeaway,'Takeaway')
        ploter.create_top_ten_pizza_plot()
        ploter.change_df(df_deliveroo,'Deliveroo')
        ploter.create_top_ten_pizza_plot()

    def answer_quest_4(self):
        print('Map locations offering kapsalons and their average price.')
        self.manager.save_to_csv_kapsalon_dfs()
        kaps_maker = MapMaker(file_paths=self.file_paths_kaps)
        kaps_maker.create_kapsalon_map_for_platform('ubereats')
        kaps_maker.create_kapsalon_map_for_platform('takeaway')
        kaps_maker.create_kapsalon_map_for_platform('deliveroo')

    def answer_quest_5(self):
        print('Comparation of top 5 categories for diferent delivery serveces.')
        df_uber = self.manager.get_top_categories('ubereats')
        df_takeaway = self.manager.get_top_categories('takeaway')
        df_deliveroo = self.manager.get_top_categories('deliveroo')
        ploter = PlotMaker(df_uber,'Ubereats')
        ploter.plot_top_categories()
        ploter.change_df(df_takeaway,'Takeaway')      
        ploter.plot_top_categories()
        ploter.change_df(df_deliveroo,'Deliveroo')
        ploter.plot_top_categories()

    def answer_aditional_q_4(self):
        df= self.manager.get_full_veg_restaurants()
        ploter = PlotMaker(df,'FullVegs')
        print(df.head())
        ploter.plot_veg_restaurants()

    def answer_all_mvp(self):
        self.answer_quest_1()
        self.answer_quest_2()
        self.answer_quest_3()
        self.answer_quest_4()
        self.answer_quest_5()