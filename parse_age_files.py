import pandas as pd
import numpy as np
import ast
import re

class Persons:

    def __init__(self, file_list):

        self.df = pd.read_table(file_list[0])

        for i in range(1, len(file_list) - 1):
            df = pd.read_table(file_list[i])
            self.df = pd.concat([self.df, df], ignore_index=True)

    def create_min_age(self):

        self.df["age"] = self.df["age"].map(lambda x: tuple(int(v) for v in re.findall("[0-9]+", x)))
        self.df['min_age'] = np.random.randn(len(self.df["age"]))

        for i in range(0, len(self.df["age"]) - 1):

            if len(self.df["age"][i]) == 0:
                self.df["min_age"][i] = None;
            else:
                self.df["min_age"][i] = self.df["age"][i][0]

    def write_age_segment_csv(self, min_age):
        directory = "/home/kuoppves/Downloads/age_images/faces/"
        result = self.df.sort(["min_age"], ascending=False)
        segment = result['min_age'].map(lambda x: x == min_age)
        sixty = result[segment]
        # Add full filepath as column
        sixty['full_filename'] = sixty["original_image"]
        # Add unique Id for files
        ids = pd.Series(np.random.randint(1, size=len(sixty['full_filename'])))
        sixty["uid"] = ids.values

        counter = 0

        file_list = []
        for i in range(0, len(sixty)):
            counter += 1

            row = sixty.iloc[i]
            filename = str(counter)
            filename += "," + directory
            filename += row['user_id']
            filename += "/coarse_tilt_aligned_face."
            filename += str(row["face_id"])
            filename += "."
            filename += row["original_image"]
            filename += "," + str(row["min_age"])
            filename += "," + str(row["gender"])
            # sixty.set_value('full_filename', i, filename)

            file_list.append(filename)

        filename = str(int(min_age)) + ".txt"
        koe = open(filename, "w")

        for line in file_list:
            print line
            koe.write(line + "\n")

        koe.close()


def main():

    # Age segments: 60-100 ; 48-53 ; 38-43 ; 25-32 ; 15-20 ; 8-12 ; 4-6

    file_list = []
    file_list.append("/home/kuoppves/Downloads/age_images/fold_0_data.txt")
    file_list.append("/home/kuoppves/Downloads/age_images/fold_1_data.txt")
    file_list.append("/home/kuoppves/Downloads/age_images/fold_2_data.txt")
    file_list.append("/home/kuoppves/Downloads/age_images/fold_3_data.txt")

    persons = Persons(file_list)
    persons.create_min_age()
    persons.write_age_segment_csv(8.0)


"""
def main():
    # Read text file which contains file info
    # Sort based age segments
    # Write file info for females over age 60
    # Format: path+filename, min_axe'\t
    directory = "/home/kuoppves/Downloads/age_images/faces/"
    filepath = "/home/kuoppves/Downloads/age_images/fold_0_data.txt"


    df = pd.read_table(filepath)
    df["age"] = df["age"].map(lambda x: tuple(int(v) for v in re.findall("[0-9]+", x)))
    #df["age"] = df["age"].map(lambia x: ast.literal_eval(x))
    #print(df["age"].dtype)
    df['min_age'] = np.random.randn(len(df["age"]))
    print(df['min_age'])
    print(len(df["age"]))
    for i in range(0, len(df["age"]) - 1):
        #print(df["min_age"][i])
        #print(df["age"][i][0])

        if len(df["age"][i]) == 0:
            df["min_age"][i] = None;
        else:
            df["min_age"][i] = df["age"][i][0]

    df.to_csv('temp.csv')

    df = pd.read_csv('temp.csv')
    # df["min_age"] = df["age"].map(lambda x: x[:][0])
    print(df["min_age"])

    result = df.sort(["min_age"], ascending=False)
    print(result)

    segment = result['min_age'].map(lambda x: x >= 60.0)
    sixty = result[segment]

    # sixty = df["min_age" >= 60.0]
    print(sixty)

    file_list = []

    print(len(sixty))

    # Add full filepath as column
    sixty['full_filename'] = sixty["original_image"]
    # Add unique Id for files
    ids = pd.Series(np.random.randint(1, size=len(sixty['full_filename'])))
    sixty["uid"] = ids.values
    print(ids.values)
    counter = 0
    for i in range(0, len(sixty)):
        counter += 1
        # row = sixty[i]
        #sixty.set_value("uid", i ,counter)
        row = sixty.iloc[i]
        filename = str(counter)
        filename += "," + directory
        filename += row['user_id']
        filename += "/coarse_tilt_aligned_face."
        filename += str(row["face_id"])
        filename += "."
        filename += row["original_image"]
        filename += "," + str(row["min_age"])
        filename += "," + str(row["gender"])
        #sixty.set_value('full_filename', i, filename)

        file_list.append(filename)

    koe = open("koe.txt", "w")

    for line in file_list:
        print line
        koe.write(line + "\n")

    koe.close()

    df3 = pd.read_csv('koe.txt', names=['full_filename','age', 'gender'])

    df2 = pd.read_csv('crowdsight.txt', names=['full_filename', 'crowdsight_age'])

    print(df3)
    print(df2)

    dfL1 = df3.set_index('full_filename', append=True)
    dfR1 = df2.set_index('full_filename', append=True)

    dfL1.join(dfR1)

    df3.merge(df2, how='left',left_on="full_filename", right_on="full_filename")

    print(df3)






    # sixty['filename'] = sixty.map(lambda x: directory + x['user_id'] + '/' + 'coarse_tilt_aligned_face.' + x['face_id'] +  + x['original_image'])

    # print(sixty['filename'])
"""

if __name__ == '__main__':
    main()
