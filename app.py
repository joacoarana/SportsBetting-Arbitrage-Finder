#%% Importamos Modulos

bs  = importlib.import_module(name="Betsson_selenium")  #BETSSON
bw  = importlib.import_module(name="BetWarrior_selenium")  #BETWARRIOR
bp  = importlib.import_module(name="Bplay_selenium")  #BPLAY
co  = importlib.import_module(name='Codere') #CODERE
sb  = importlib.import_module(name='Sportsbet') #SPORTSBET.IO
oxb = importlib.import_module(name="OneXBet")  #ONEXBET
#%%
import concurrent.futures
import pandas as pd
from fuzzywuzzy import fuzz
import requests

#%%



class SportsBettingAnalyzer:
    def __init__(self):
        eng = [
               'https://pba.betsson.bet.ar/apuestas-deportivas/futbol/inglaterra/inglaterra-premier-league-epl',
               'https://pba.betwarrior.bet.ar/es-ar/sports/futbol/inglaterra/premier-league',
               'https://deportespba.bplay.bet.ar/competicion/94-premier-league',
               'https://ar.1xbet.com/es/line/football/88637-england-premier-league',
               'https://sportsbet.io/es/sports/soccer/england/premier-league/matches'
               ]

        ita = [
               'https://pba.betsson.bet.ar/apuestas-deportivas/futbol/italia/italia-serie-a',
               'https://pba.betwarrior.bet.ar/es-ar/sports/futbol/italia/serie-a',
               'https://deportespba.bplay.bet.ar/competicion/305-serie-a',
               'https://1xbet.com/es/line/football/110163-italy-serie-a',
               'https://sportsbet.io/es/sports/soccer/italy/serie-a/matches'
               ]

        fra = [
               'https://pba.betsson.bet.ar/apuestas-deportivas/futbol/francia/francia-ligue-1',
               'https://pba.betwarrior.bet.ar/es-ar/sports/futbol/francia/ligue-1',
               'https://deportespba.bplay.bet.ar/competicion/96-ligue-1',
               'https://ar.1xbet.com/line/football/12821-france-ligue-1',
               'https://sportsbet.io/es/sports/soccer/france/ligue-1/matches'
               ]

        esp = [
               'https://pba.betsson.bet.ar/apuestas-deportivas/futbol/espana/espana-la-liga',
               'https://pba.betwarrior.bet.ar/es-ar/sports/futbol/espana',
               'https://deportespba.bplay.bet.ar/competicion/306-laliga',
               'https://ar.1xbet.com/line/football/127733-spain-la-liga',
               'https://sportsbet.io/es/sports/soccer/spain/la-liga/matches'
               ]

        ger = [
               'https://pba.betsson.bet.ar/apuestas-deportivas/futbol/alemania/alemania-bundesliga',
               'https://pba.betwarrior.bet.ar/es-ar/sports/futbol/alemania/bundesliga',
               'https://deportespba.bplay.bet.ar/competicion/268-bundesliga',
               'https://ar.1xbet.com/line/football/96463-germany-bundesliga',
               'https://sportsbet.io/es/sports/soccer/germany/bundesliga/matches'
               ]

        arg = [
               'https://pba.betsson.bet.ar/apuestas-deportivas/futbol/argentina/liga-profesional',
               'https://pba.betwarrior.bet.ar/es-ar/sports/futbol/argentina/liga-profesional-argentina',
               'https://deportespba.bplay.bet.ar/competicion/2530-liga-profesional-argentina',
               'https://ar.1xbet.com/line/football/119599-argentina-primera-division',
               'https://sportsbet.io/es/sports/soccer/argentina/superliga/matches'       
               ]

        wc_f = [
                'https://pba.betsson.bet.ar/apuestas-deportivas/futbol/copa-mundial-femenina/copa-mundial-femenina',
                'https://pba.betwarrior.bet.ar/es-ar/sports/futbol/copa-mundial-femenina',
                'https://deportespba.bplay.bet.ar/competicion/45272-copa-del-mundo-f',
                '',
                'https://sportsbet.io/es/sports/soccer/international/world-cup-women/matches'
               ]
        
        ucl = [
                'https://pba.betsson.bet.ar/apuestas-deportivas/futbol/champions-league/liga-de-campeones',
                'https://pba.betwarrior.bet.ar/es-ar/sports/futbol/clasificacion-de-la-champions-league',
                'https://deportespba.bplay.bet.ar/competicion/6674-champions-league',
                'https://1xbet.com/line/football/118587-uefa-champions-league',
                'https://sportsbet.io/es/sports/soccer/international-clubs/uefa-champions-league/matches'
            ]
        
        sue = [
            'https://pba.betsson.bet.ar/apuestas-deportivas/futbol/suecia/suecia-allsvenskan',
            'https://pba.betwarrior.bet.ar/es-ar/sports/futbol/suecia/allsvenskan',
            'https://deportespba.bplay.bet.ar/competicion/99-allsvenskan',
            'https://1xbet.com/line/football/212425-sweden-allsvenskan',
            'https://sportsbet.io/es/sports/soccer/sweden/allsvenskan/matches'
            ]
        
        den = [
            'https://pba.betsson.bet.ar/apuestas-deportivas/futbol/dinamarca/superliga',
            'https://pba.betwarrior.bet.ar/es-ar/sports/futbol/dinamarca/superligaen',
            'https://deportespba.bplay.bet.ar/competicion/130-superligaen',
            'https://1xbet.com/line/football/8773-denmark-superliga',
            'https://sportsbet.io/es/sports/soccer/denmark/superligaen/matches'
            ]
        
        est = [
            'https://pba.betsson.bet.ar/apuestas-deportivas/futbol/europa/estonia-meistriliiga',
            '',
            'https://deportespba.bplay.bet.ar/competicion/42922-meistriliiga',
            'https://1xbet.com/es/line/football/33033-estonia-meistriliiga',
            ''
            ]
        
        fin = [
            'https://pba.betsson.bet.ar/apuestas-deportivas/futbol/finlandia/veikkausliiga-finlandesa',
            'https://pba.betwarrior.bet.ar/es-ar/sports/futbol/finlandia/veikkausliiga',
            'https://deportespba.bplay.bet.ar/competicion/29-veikkausliiga',
            'https://1xbet.com/line/football/1554897-finland-veikkausliiga',
            'https://sportsbet.io/es/sports/soccer/finland/veikkausliiga/matches'
            ]
        
        tur = [
            'https://pba.betsson.bet.ar/apuestas-deportivas/futbol/turquia/super-ligi-turca',
            '',
            '',
            'https://1xbet.com/es/line/football/11113-turkey-superliga',
            ''            
            ]
        
        self.bs_dict =  {'eng': eng[0], 'ita': ita[0], 'fra': fra[0], 'esp': esp[0], 'ger': ger[0], 'arg': arg[0], 'wc_f' : wc_f[0],'ucl': ucl[0], 'sue': sue[0], 'den': den[0], 'est': est[0], 'fin': fin[0], 'tur': tur[0]}  # Replace with your data dictionaries for Betsson, Betwarrior, etc.
        self.bw_dict =  {'eng': eng[1], 'ita': ita[1], 'fra': fra[1], 'esp': esp[1], 'ger': ger[1], 'arg': arg[1], 'wc_f' : wc_f[1],'ucl': ucl[1], 'sue': sue[1], 'den': den[1], 'est': est[1], 'fin': fin[1], 'tur': tur[1]}
        self.bp_dict =  {'eng': eng[2], 'ita': ita[2], 'fra': fra[2], 'esp': esp[2], 'ger': ger[2], 'arg': arg[2], 'wc_f' : wc_f[2],'ucl': ucl[2], 'sue': sue[2], 'den': den[2], 'est': est[2], 'fin': fin[2], 'tur': tur[2]}
        self.oxb_dict =  {'eng': eng[3], 'ita': ita[3], 'fra': fra[3], 'esp': esp[3], 'ger': ger[3], 'arg': arg[3], 'wc_f' : wc_f[3],'ucl': ucl[3], 'sue': sue[3], 'den': den[3], 'est': est[3], 'fin': fin[3],'tur': tur[3]}
        self.sb_dict = {'eng': eng[4], 'ita': ita[4], 'fra': fra[4], 'esp': esp[4], 'ger': ger[4], 'arg': arg[4], 'wc_f' : wc_f[4],'ucl': ucl[4], 'sue': sue[4], 'den': den[4], 'est': est[4], 'fin': fin[4], 'tur': tur[4]}
        
        self.ligas= ['eng', 'ita', 'fra', 'esp', 'ger', 'arg', 'wc_f', 'ucl', 'sue', 'den', 'est', 'fin', 'tur']
        
        
    def get_betsson_data(self, str_liga):
        try:
            return bs.Betsson(self.bs_dict[str_liga])
        except:
            return []
    
    def get_betwarrior_data(self, str_liga):
        try:
            return bw.BetWarrior(self.bw_dict[str_liga])
        except:
            return []
    
    def get_bplay_data(self, str_liga):
        try:
            return bp.BPlay(self.bp_dict[str_liga])
        except:
            return []
    
    def get_codere_data(self, str_liga):
        try:
            return co.Codere(str_liga)
        except:
            return []
    
    def get_sportsbet_data(self, str_liga):
        try:        
            return sb.Sportsbet(self.sb_dict[str_liga])
        except:
            return[]
        
    
    def get_onexbet_data(self, str_liga):
        try:
            return oxb.OneXBet(self.oxb_dict[str_liga])
        except:
            return []
        
    # def Liga_2(self):
    #     Betsson     = []
    #     Betwarrior  = []
    #     Bplay       = []
    #     Codere      = []
    #     Sportsbet   = []
    #     OneXBet     = []

        
        
    #     with concurrent.futures.ThreadPoolExecutor() as executor:
    #         for liga in self.ligas:    
    #             future_betsson = executor.submit(self.get_betsson_data, liga)
    #             Betsson_list = future_betsson.result()
    #             Betsson.append(Betsson_list)
    #     print(Betsson)
        
    #     with concurrent.futures.ThreadPoolExecutor() as executor:
    #         for liga in self.ligas:    
    #             future_betwarrior = executor.submit(self.get_betwarrior_data, liga)
    #             Betwarrior_list = future_betwarrior.result()
    #             Betwarrior.append(Betwarrior_list)
        
    #     with concurrent.futures.ThreadPoolExecutor() as executor:
    #         for liga in self.ligas:    
    #             future_bplay = executor.submit(self.get_bplay_data, liga)
    #             Bplay_list = future_bplay.result()
    #             Bplay.append(Bplay_list)
        
    #     with concurrent.futures.ThreadPoolExecutor() as executor:
    #         for liga in self.ligas:    
    #             future_codere = executor.submit(self.get_codere_data, liga)
    #             Codere_list = future_codere.result()
    #             Codere.append(Codere_list)
                
    #     with concurrent.futures.ThreadPoolExecutor() as executor:
    #         for liga in self.ligas:    
    #             future_sportsbet = executor.submit(self.get_sportsbet_data, liga)
    #             Sportsbet_list = future_sportsbet.result()
    #             Sportsbet.append(Sportsbet_list)        
        
    #     with concurrent.futures.ThreadPoolExecutor() as executor:
    #         for liga in self.ligas:    
    #             future_onexbet = executor.submit(self.get_onexbet_data, liga)
    #             OneXbet_list = future_onexbet.result()
    #             OneXBet.append(OneXbet_list)
        
                
    #     return Betsson, Betwarrior, Bplay, Codere, Sportsbet, OneXBet
    
    def Liga_2(self):
        Betsson = []
        Betwarrior = []
        Bplay = []
        Codere = []
        Sportsbet = []
        OneXBet = []
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
                # Submit tasks for all sources and store the futures
            betsson_futures = [executor.submit(self.get_betsson_data, liga) for liga in self.ligas]
            betwarrior_futures = [executor.submit(self.get_betwarrior_data, liga) for liga in self.ligas]
            bplay_futures = [executor.submit(self.get_bplay_data, liga) for liga in self.ligas]
            codere_futures = [executor.submit(self.get_codere_data, liga) for liga in self.ligas]
            sportsbet_futures = [executor.submit(self.get_sportsbet_data, liga) for liga in self.ligas]
            onexbet_futures = [executor.submit(self.get_onexbet_data, liga) for liga in self.ligas]
        
            # Gather results for Betsson
            Betsson = [future.result() for future in betsson_futures]
            # Gather results for Betwarrior
            Betwarrior = [future.result() for future in betwarrior_futures]
            # Gather results for Bplay
            Bplay = [future.result() for future in bplay_futures]
            # Gather results for Codere
            Codere = [future.result() for future in codere_futures]
            # Gather results for Sportsbet
            Sportsbet = [future.result() for future in sportsbet_futures]
            # Gather results for OneXBet
            OneXBet = [future.result() for future in onexbet_futures]
        
        return Betsson, Betwarrior, Bplay, Codere, Sportsbet, OneXBet
    
    def Liga(self, str_liga):
        
        # Create a ThreadPoolExecutor
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit the functions for execution
            future_betsson = executor.submit(self.get_betsson_data, str_liga)
            future_betwarrior = executor.submit(self.get_betwarrior_data, str_liga)
            future_bplay = executor.submit(self.get_bplay_data, str_liga)
            future_codere = executor.submit(self.get_codere_data, str_liga)
            future_sportsbet = executor.submit(self.get_sportsbet_data, str_liga)
            future_onexbet = executor.submit(self.get_onexbet_data, str_liga)

            # Wait for all futures to complete and get the results
            Betsson_list = future_betsson.result()
            # print(Betsson_list)
            Betwarrior_list = future_betwarrior.result()
            Bplay_list = future_bplay.result()
            Codere_list = future_codere.result()
            Sportsbet_list = future_sportsbet.result()
            OneXbet_list = future_onexbet.result()
            
        return Betsson_list, Betwarrior_list, Bplay_list, Codere_list, Sportsbet_list, OneXbet_list

    def add_game_key(self, match_list):
        if not match_list:
            return

        for match in match_list:
            teams = list(match.keys())
            game_name = f"{teams[0]} vs {teams[2]}"
            match['game'] = game_name

    def modify_keys_in_dicts(self, match_list, list_number):
        if not match_list:
            return

        for match in match_list:
            keys_to_modify = list(match.keys())
            for key in keys_to_modify:
                if key != 'game':
                    new_key = f"{key}_{list_number}"
                    if 'Home' not in match:
                        match['Home'] = match.pop(key)
                    elif 'Draw' not in match:
                        match['Draw'] = match.pop(key)
                    elif 'Away' not in match:
                        match['Away'] = match.pop(key)

    def create_dataframe_with_suffix(self, data_list, suffix):
        try:
            df = pd.DataFrame(data_list).set_index('game').rename(columns=lambda x: f"{x}_{suffix}")
        except (TypeError, ValueError, KeyError):
            df = pd.DataFrame()  # Return an empty DataFrame if an error occurs
        return df

    def remove_duplicate_rows(self, df):
        df_no_duplicates = df[~df.index.duplicated(keep='first')]
        return df_no_duplicates

    def remove_numbers_and_dots_from_string(self, s):
        return ''.join(filter(lambda x: not (x.isdigit() or x == '.'), s))

    def merge_matching_strings_rows(self, df):
        new_df = df.copy()

        for idx1 in df.index:
            substrings_list = idx1.split()
            for idx2 in df.index:
                if idx1 != idx2 and all(word in idx2 for word in substrings_list):
                    merged_row = pd.concat([df.loc[idx1], df.loc[idx2]], axis=0)
                    merged_row = merged_row.groupby(merged_row.index).first()
                    new_df.drop(index=[idx1, idx2], inplace=True, errors='ignore')
                    new_df.loc[idx1] = merged_row

        return new_df

    def merge_similar_rows(self, df, fuzz_ratio):
        similar_indexes = {}
        index_copy = df.index.copy()  # Make a copy of the DataFrame's index

        for idx1 in index_copy:
            idx1.replace("Femenino", "")
            for idx2 in index_copy:
                idx2.replace("Femenino", "")
                if idx1 != idx2 and fuzz.ratio(idx1, idx2)>fuzz_ratio:
                    # idx1_parts = idx1.split(" vs ")
                    # idx2_parts = idx2.split(" vs ")
                    # similarity_before = fuzz.ratio(idx1_parts[0], idx2_parts[0])
                    # similarity_after = fuzz.ratio(idx1_parts[1], idx2_parts[1])
                    # if similarity_before > fuzz_ratio and similarity_after > fuzz_ratio:
                        similar_indexes[idx1] = similar_indexes.get(idx1, []) + [idx2]
        new_df = df.copy()

        for idx1, similar_idxs in similar_indexes.items():
            merged_row = pd.Series(dtype='object')
            for similar_idx in similar_idxs + [idx1]:
                if similar_idx in df.index:  # Check if the row still exists in the DataFrame
                    merged_row = pd.concat([merged_row, df.loc[similar_idx]], axis=0)

            merged_row = merged_row.groupby(merged_row.index).first()
            new_df.drop(index=similar_idxs, inplace=True, errors='ignore')  # Ignore errors if a row doesn't exist
            new_df.loc[idx1] = merged_row

        return new_df

    def compute_df_2(self):
        
        all_merged_df = pd.DataFrame()
        Betsson, Betwarrior, Bplay, Codere, Sportsbet, OneXBet = self.Liga_2()
            
        for i in range (len (self.ligas)):
            
            str_liga = self.ligas[i]
            
            Betsson_list        = Betsson[i]
            Betwarrior_list     = Betwarrior[i]
            Bplay_list          = Bplay[i]
            Codere_list         = Codere[i]  
            Sportsbet_list      = Sportsbet[i]
            OneXbet_list        = OneXBet[i]
            
            # Add 'game' key for each match in the lists
            self.add_game_key(Betsson_list)
            self.add_game_key(Betwarrior_list)
            self.add_game_key(Bplay_list)
            self.add_game_key(Codere_list)
            self.add_game_key(Sportsbet_list)
            self.add_game_key(OneXbet_list)
            
            # Modify keys in all dictionaries
            self.modify_keys_in_dicts(Betsson_list, 'bs')
            self.modify_keys_in_dicts(Betwarrior_list, 'bw')
            self.modify_keys_in_dicts(Bplay_list, 'bp')
            self.modify_keys_in_dicts(Codere_list, 'co')
            self.modify_keys_in_dicts(Sportsbet_list, 'sb')
            self.modify_keys_in_dicts(OneXbet_list, 'oxb')
            
            df1 = self.create_dataframe_with_suffix(Betsson_list, 'bs')
            df2 = self.create_dataframe_with_suffix(Betwarrior_list, 'bw')
            df3 = self.create_dataframe_with_suffix(Bplay_list, 'bp')
            df4 = self.create_dataframe_with_suffix(Codere_list, 'co')
            df5 = self.create_dataframe_with_suffix(Sportsbet_list, 'sb')
            df6 = self.create_dataframe_with_suffix(OneXbet_list, 'oxb')
            
            # Check and remove duplicate rows for each DataFrame
            df1 = self.remove_duplicate_rows(df1)
            df2 = self.remove_duplicate_rows(df2)
            df3 = self.remove_duplicate_rows(df3)
            df4 = self.remove_duplicate_rows(df4)    
            df5 = self.remove_duplicate_rows(df5)
            df6 = self.remove_duplicate_rows(df6)
            
            print(f'Betsson: {len(df1)}')
            print(f'Betwarrior: {len(df2)}')
            print(f'Bplay: {len(df3)}')
            print(f'Codere: {len(df4)}')
            print(f'Sportsbet: {len(df5)}')
            print(f'OneXbet: {len(df6)}')
            
            min_len = max(len(df1), len(df2), len(df3), len(df4), len(df5), len(df6))
            
            # Merge matching strings rows and similar rows based on fuzz ratio
            merged_simple = pd.concat([df1, df2, df3, df4, df5, df6], axis=1)
            
            merged_simple.index = merged_simple.index.map(self.remove_numbers_and_dots_from_string)
            
            merged = self.merge_matching_strings_rows(merged_simple)
            
            fuzz_ratio = 60  # Initial fuzz ratio
            
            merged_df=self.merge_similar_rows(merged, fuzz_ratio)
            
            merged_df.dropna(how='all', inplace=True)
            
            if len(merged_df) >= min_len:
                
                # print (merged_df)        
                all_merged_df= all_merged_df.append(merged_df)
            
            else:
                
                while len(merged_df) <= min_len:
                    fuzz_ratio += 0.25
                    merged_df=self.merge_similar_rows(merged, fuzz_ratio)
                    merged_df.dropna(how='all', inplace=True)
                all_merged_df= all_merged_df.append(merged_df)
            
        return all_merged_df
    
    def compute_df(self, str_liga):   
        Betsson_list, Betwarrior_list, Bplay_list, Codere_list, Sportsbet_list, OneXbet_list = self.Liga(str_liga)
        
        # Add 'game' key for each match in the lists
        self.add_game_key(Betsson_list)
        self.add_game_key(Betwarrior_list)
        self.add_game_key(Bplay_list)
        self.add_game_key(Codere_list)
        self.add_game_key(Sportsbet_list)
        self.add_game_key(OneXbet_list)
        
        # Modify keys in all dictionaries
        self.modify_keys_in_dicts(Betsson_list, 'bs')
        self.modify_keys_in_dicts(Betwarrior_list, 'bw')
        self.modify_keys_in_dicts(Bplay_list, 'bp')
        self.modify_keys_in_dicts(Codere_list, 'co')
        self.modify_keys_in_dicts(Sportsbet_list, 'sb')
        self.modify_keys_in_dicts(OneXbet_list, 'oxb')
        
        df1 = self.create_dataframe_with_suffix(Betsson_list, 'bs')
        df2 = self.create_dataframe_with_suffix(Betwarrior_list, 'bw')
        df3 = self.create_dataframe_with_suffix(Bplay_list, 'bp')
        df4 = self.create_dataframe_with_suffix(Codere_list, 'co')
        df5 = self.create_dataframe_with_suffix(Sportsbet_list, 'sb')
        df6 = self.create_dataframe_with_suffix(OneXbet_list, 'oxb')
        
        # Check and remove duplicate rows for each DataFrame
        df1 = self.remove_duplicate_rows(df1)
        df2 = self.remove_duplicate_rows(df2)
        df3 = self.remove_duplicate_rows(df3)
        df4 = self.remove_duplicate_rows(df4)    
        df5 = self.remove_duplicate_rows(df5)
        df6 = self.remove_duplicate_rows(df6)
        
        print(f'Betsson: {len(df1)}')
        print(f'Betwarrior: {len(df2)}')
        print(f'Bplay: {len(df3)}')
        print(f'Codere: {len(df4)}')
        print(f'Sportsbet: {len(df5)}')
        print(f'OneXbet: {len(df6)}')
        
        min_len = max(len(df1), len(df2), len(df3), len(df4), len(df5), len(df6))
        
        # Merge matching strings rows and similar rows based on fuzz ratio
        merged_simple = pd.concat([df1, df2, df3, df4, df5, df6], axis=1)
        
        merged_simple.index = merged_simple.index.map(self.remove_numbers_and_dots_from_string)
        
        merged = self.merge_matching_strings_rows(merged_simple)
        
        fuzz_ratio = 65  # Initial fuzz ratio
        
        merged_df=self.merge_similar_rows(merged, fuzz_ratio)
        
        merged_df.dropna(how='all', inplace=True)
        
        if len(merged_df) >= min_len:
            
            # print (merged_df)        
            return merged_df
        
        else:
            
            while len(merged_df) <= min_len:
                fuzz_ratio += 0.25
                merged_df=self.merge_similar_rows(merged, fuzz_ratio)
                merged_df.dropna(how='all', inplace=True)
        
        return merged_df

    def extract_max_odds(self, df):
        max_odds_df = pd.DataFrame()

        for index, row in df.iterrows():
            home_columns = [col for col in row.index if 'Home' in col]
            draw_columns = [col for col in row.index if 'Draw' in col]
            away_columns = [col for col in row.index if 'Away' in col]

            home_max_odds = row[home_columns].max()
            home_max_info = row[home_columns].idxmax().split('_')[-1]
            draw_max_odds = row[draw_columns].max()
            draw_max_info = row[draw_columns].idxmax().split('_')[-1]
            away_max_odds = row[away_columns].max()
            away_max_info = row[away_columns].idxmax().split('_')[-1]

            tiv = 1 / home_max_odds + 1 / draw_max_odds + 1 / away_max_odds

            max_odds_df.at[index, 'Max_Home_Info'] = home_max_info
            max_odds_df.at[index, 'Max_Home_Odds'] = home_max_odds

            max_odds_df.at[index, 'Max_Draw_Info'] = draw_max_info
            max_odds_df.at[index, 'Max_Draw_Odds'] = draw_max_odds

            max_odds_df.at[index, 'Max_Away_Info'] = away_max_info
            max_odds_df.at[index, 'Max_Away_Odds'] = away_max_odds

            max_odds_df.at[index, 'TIV'] = tiv
            
            filtered_rows = max_odds_df[max_odds_df['TIV'] < 1]
            
            # print(filtered_rows)
            # print(max_odds_df)
            # print('hi')

        return filtered_rows, max_odds_df

    def calculate_implied_probabilities(self, row):
        implied_prob_home = 1 / row['Max_Home_Odds']
        implied_prob_draw = 1 / row['Max_Draw_Odds']
        implied_prob_away = 1 / row['Max_Away_Odds']
        
        return implied_prob_home, implied_prob_draw, implied_prob_away

    def arbitrage(self, filtered_rows):
        try:
            implied_probs = filtered_rows.apply(self.calculate_implied_probabilities, axis=1, result_type='expand')
            filtered_rows['Implied_Prob_Home'] = implied_probs[0]
            filtered_rows['Implied_Prob_Draw'] = implied_probs[1]
            filtered_rows['Implied_Prob_Away'] = implied_probs[2]
    
            arbitrage_opportunity = filtered_rows[filtered_rows['TIV'] < 1].copy()
    
            arbitrage_opportunity['Bet_Percentage_Home'] = arbitrage_opportunity['Implied_Prob_Home'] / arbitrage_opportunity['TIV']
            arbitrage_opportunity['Bet_Percentage_Draw'] = arbitrage_opportunity['Implied_Prob_Draw'] / arbitrage_opportunity['TIV']
            arbitrage_opportunity['Bet_Percentage_Away'] = arbitrage_opportunity['Implied_Prob_Away'] / arbitrage_opportunity['TIV']
    
            arbitrage_opportunity['%WIN1'] = (arbitrage_opportunity['Bet_Percentage_Home'] * arbitrage_opportunity['Max_Home_Odds'] - 1) * 100
            arbitrage_opportunity['%WIN2'] = (arbitrage_opportunity['Bet_Percentage_Draw'] * arbitrage_opportunity['Max_Draw_Odds'] - 1) * 100
            arbitrage_opportunity['%WIN3'] = (arbitrage_opportunity['Bet_Percentage_Away'] * arbitrage_opportunity['Max_Away_Odds'] - 1) * 100
            return arbitrage_opportunity
        except:
            print(f'No hay Arbitraje en la liga')
        

    def analyze(self, str_liga):
        merged_df = self.compute_df(str_liga)
        filtered_rows, max_odds_df = self.extract_max_odds(merged_df)
        return self.arbitrage(filtered_rows), max_odds_df
    
    def analyze_all_2(self):
        all_merged_df = self.compute_df_2()
        filtered_rows, max_odds_df = self.extract_max_odds(all_merged_df)
        return self.arbitrage(filtered_rows), max_odds_df
        

    def analyze_all(self):
        all_arbitrages = pd.DataFrame()
        odds = pd.DataFrame()
        for liga in self.ligas:
            print(liga)
            row, maxodd = self.analyze(liga)
            all_arbitrages=all_arbitrages.append(row) 
            odds=odds.append(maxodd)
        return all_arbitrages, odds
    
    
    def send_dataframe_to_channel(self, df):
        # Initialize the message string
        message = ""
    
        # Iterate through the DataFrame rows
        for index, row in df.iterrows():
            # Extract the relevant information from each row
            match_info = f"{index}\n\n"
            home_team = row["Max_Home_Info"]
            home_odds = row["Max_Home_Odds"]
            draw_info = row["Max_Draw_Info"]
            draw_odds = row["Max_Draw_Odds"]
            away_team = row["Max_Away_Info"]
            away_odds = row["Max_Away_Odds"]
            bet_percentage_home = row["Bet_Percentage_Home"]
            bet_percentage_draw = row["Bet_Percentage_Draw"]
            bet_percentage_away = row["Bet_Percentage_Away"]
            win1 = row["%WIN1"]
            win2 = row["%WIN2"]
            win3 = row["%WIN3"]
    
            # Create a formatted message for each row
            row_message = f"📣 *{match_info}*"
            row_message += f"🟦 Home: ---{home_team}--- *({home_odds})*\n"
            row_message += f"🟨 Draw: ---{draw_info}--- *({draw_odds})*\n"
            row_message += f"🟥 Away: ---{away_team}--- *({away_odds})*\n\n"
            row_message += f"Home = {bet_percentage_home:.4}\n"
            row_message += f"Draw = {bet_percentage_draw:.4}\n"
            row_message += f"Away = {bet_percentage_away:.4}\n\n"
            row_message += f"💰 _GANANCIA :_ *{win1:.5}%*\n\n"

            # Append the row message to the overall message
            message += row_message
    
        # API URL and data for Telegram message
        api_url = ""
        data = {
            "chat_id": "",
            "text": message,
            "parse_mode": "Markdown"  # Specify Markdown mode for formatting
        }
    
        # Send the message using the requests library
        response = requests.post(api_url, data=data)
    
        # Return the response JSON
        return response.json()
    
    def Telegram(self):
        all_arbitrages, max_odds= self.analyze_all()
        return self.send_dataframe_to_channel(all_arbitrages), max_odds
    
    def Telegram_2(self):
        all_arbitrages, max_odds= self.analyze_all_2()
        return self.send_dataframe_to_channel(all_arbitrages), max_odds
        

#%%

a= SportsBettingAnalyzer()
a.Telegram()
