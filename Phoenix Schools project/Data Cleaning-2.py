{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "34dbed5b",
   "metadata": {},
   "source": [
    "# Project Step 3\n",
    "### Date: 03/07/2024\n",
    "\n",
    "##### Vinaya Madhulikha Polisetti \n",
    "##### Deepika Ramya Sri Tenela \n",
    "##### Ruthvik Reddy Aileni \n",
    "##### Maneesh Gandra\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fec77a1e-3364-4ec9-9123-1c6d10a90400",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Before cleaning:  (346, 19)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "dt = pd.read_csv('dataset.csv')\n",
    "\n",
    "print(\"Before cleaning: \",dt.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3d3d118e",
   "metadata": {},
   "source": [
    "### Step 1:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "09c8d08f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Missing values per column:\n",
      "\n",
      "School                                    0\n",
      "City                                      0\n",
      "Zip Code                                  0\n",
      "2023 Student Enrollments                 41\n",
      "AZ Rank                                 182\n",
      "Student Teacher Ratio                   134\n",
      "Graduation Rate%                        155\n",
      "Dual Enrollment                           7\n",
      "Offers Electives                          8\n",
      "Free Lunch (%)                          168\n",
      "Mental Health Services                    6\n",
      "Racial %   White                         63\n",
      "Racial %   Asian                         92\n",
      "Racial %   Hispanic                      59\n",
      "Gender   Male                           103\n",
      "Gender   Female                         103\n",
      "AP Classes                               13\n",
      "School Grade                            116\n",
      "Inexperienced Core Acadamic Teachers     56\n",
      "dtype: int64\n",
      "\n",
      "Missing values per row:\n",
      "\n",
      "0      2\n",
      "1      2\n",
      "2      5\n",
      "3      0\n",
      "4      4\n",
      "      ..\n",
      "341    3\n",
      "342    0\n",
      "343    1\n",
      "344    2\n",
      "345    3\n",
      "Length: 346, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "\n",
    "missing_col = dt.isnull().sum()\n",
    "missing_row = dt.isnull().sum(axis=1)\n",
    "\n",
    "print(\"Missing values per column:\\n\")\n",
    "print(missing_col)\n",
    "print(\"\\nMissing values per row:\\n\")\n",
    "print(missing_row)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1de87a50-a1c6-4672-9130-219427c38e69",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After removing null values: (166, 15)\n"
     ]
    }
   ],
   "source": [
    "# Drop columns with a high number of missing values\n",
    "cols_drop = ['AZ Rank', 'Student Teacher Ratio', 'Graduation Rate%', 'Free Lunch (%)']\n",
    "dt_cleaned = dt.drop(columns = cols_drop)\n",
    "\n",
    "# Drop rows with missing values \n",
    "dt_cleaned = dt_cleaned.dropna()\n",
    "\n",
    "print(\"After removing null values:\",dt_cleaned.shape)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "80a7191d",
   "metadata": {},
   "source": [
    "### Step 2:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0dea1c89",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of rows with Duplicates: 0\n",
      "After removing duplicates (166, 15)\n"
     ]
    }
   ],
   "source": [
    "\n",
    "dups = dt_cleaned.duplicated(subset=['School', 'Zip Code'], keep='first')\n",
    "\n",
    "print(\"Number of rows with Duplicates:\", dups.sum())\n",
    "\n",
    "dt_cleaned.drop_duplicates(subset=['School', 'Zip Code'], inplace=True)\n",
    "print(\"After removing duplicates\",dt_cleaned.shape)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c67fd904",
   "metadata": {},
   "source": [
    "### Step 3:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "88709e5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "numeric_cols = dt_cleaned.select_dtypes(include='number').columns\n",
    "dt_cleaned[numeric_cols] = dt_cleaned[numeric_cols].replace({'\\$': '', '%': ''}, regex=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "191ec825",
   "metadata": {},
   "outputs": [],
   "source": [
    "dt_cleaned['AP Classes'] = dt_cleaned['AP Classes'].str.upper().str.strip()\n",
    "dt_cleaned['Dual Enrollment'] = dt_cleaned['Dual Enrollment'].str.upper().str.strip()\n",
    "dt_cleaned['Offers Electives'] = dt_cleaned['Offers Electives'].str.upper().str.strip()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "63586415",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['A', 'B', 'C', 'D', 'A+', 'C+', 'C ', 'D ', 'B ', 'B+', 'D+', 'A ']\n"
     ]
    }
   ],
   "source": [
    "# transforming ordinal data: School Grade\n",
    "\n",
    "print(dt_cleaned['School Grade'].unique().tolist())\n",
    "\n",
    "grd = {\n",
    "    'A+':8,\n",
    "    'A':7,\n",
    "    'B+':6,\n",
    "    'B':5,\n",
    "    'C+':4,\n",
    "    'C':3,\n",
    "    'D+':2,\n",
    "    'D':1,\n",
    "}\n",
    "\n",
    "dt_cleaned['School Grade'] = dt_cleaned['School Grade'].map(grd)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2ba5e4b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Transforming categorical variables\n",
    "\n",
    "cts = ['School','City','Dual Enrollment','Offers Electives', 'Mental Health Services','AP Classes'] \n",
    "\n",
    "for ct in cts:\n",
    "    if ct in ['School','City']:\n",
    "        a = pd.get_dummies(dt_cleaned[ct], dtype=int)\n",
    "    else:\n",
    "        a = pd.get_dummies(dt_cleaned[ct], prefix=ct, dtype=int)\n",
    "    dt_cleaned = pd.concat([dt_cleaned,a], axis=1)\n",
    "\n",
    "dt_cleaned = dt_cleaned.drop(columns = cts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "bea89138",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Zip Code</th>\n",
       "      <th>2023 Student Enrollments</th>\n",
       "      <th>Racial %   White</th>\n",
       "      <th>Racial %   Asian</th>\n",
       "      <th>Racial %   Hispanic</th>\n",
       "      <th>Gender   Male</th>\n",
       "      <th>Gender   Female</th>\n",
       "      <th>School Grade</th>\n",
       "      <th>Inexperienced Core Acadamic Teachers</th>\n",
       "      <th>Aaec   Smcc Campus</th>\n",
       "      <th>...</th>\n",
       "      <th>Peoria. AZ</th>\n",
       "      <th>Phoenix,AZ</th>\n",
       "      <th>Dual Enrollment_NO</th>\n",
       "      <th>Dual Enrollment_YES</th>\n",
       "      <th>Offers Electives_NO</th>\n",
       "      <th>Offers Electives_YES</th>\n",
       "      <th>Mental Health Services_False</th>\n",
       "      <th>Mental Health Services_True</th>\n",
       "      <th>AP Classes_NO</th>\n",
       "      <th>AP Classes_YES</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>85086</td>\n",
       "      <td>196</td>\n",
       "      <td>66.86</td>\n",
       "      <td>8.36</td>\n",
       "      <td>15.26</td>\n",
       "      <td>467.0</td>\n",
       "      <td>559.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>25.0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>85323</td>\n",
       "      <td>1608</td>\n",
       "      <td>12.16</td>\n",
       "      <td>1.88</td>\n",
       "      <td>71.69</td>\n",
       "      <td>805.0</td>\n",
       "      <td>822.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>14.0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>85338</td>\n",
       "      <td>1715</td>\n",
       "      <td>40.72</td>\n",
       "      <td>1.94</td>\n",
       "      <td>46.55</td>\n",
       "      <td>1058.0</td>\n",
       "      <td>912.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>85338</td>\n",
       "      <td>1225</td>\n",
       "      <td>41.09</td>\n",
       "      <td>31.98</td>\n",
       "      <td>14.66</td>\n",
       "      <td>1051.0</td>\n",
       "      <td>969.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>8.0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>85338</td>\n",
       "      <td>2420</td>\n",
       "      <td>59.89</td>\n",
       "      <td>10.98</td>\n",
       "      <td>17.48</td>\n",
       "      <td>1505.0</td>\n",
       "      <td>1371.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>11.0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 194 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    Zip Code 2023 Student Enrollments Racial %   White  Racial %   Asian  \\\n",
       "1      85086                      196            66.86              8.36   \n",
       "3      85323                     1608            12.16              1.88   \n",
       "17     85338                     1715            40.72              1.94   \n",
       "22     85338                     1225            41.09             31.98   \n",
       "24     85338                     2420            59.89             10.98   \n",
       "\n",
       "    Racial %   Hispanic  Gender   Male  Gender   Female  School Grade  \\\n",
       "1                 15.26          467.0            559.0           7.0   \n",
       "3                 71.69          805.0            822.0           5.0   \n",
       "17                46.55         1058.0            912.0           7.0   \n",
       "22                14.66         1051.0            969.0           7.0   \n",
       "24                17.48         1505.0           1371.0           7.0   \n",
       "\n",
       "    Inexperienced Core Acadamic Teachers  Aaec   Smcc Campus  ...  Peoria. AZ  \\\n",
       "1                                   25.0                   0  ...           0   \n",
       "3                                   14.0                   0  ...           0   \n",
       "17                                   5.0                   0  ...           0   \n",
       "22                                   8.0                   0  ...           0   \n",
       "24                                  11.0                   0  ...           0   \n",
       "\n",
       "    Phoenix,AZ  Dual Enrollment_NO  Dual Enrollment_YES  Offers Electives_NO  \\\n",
       "1            0                   0                    1                    0   \n",
       "3            0                   0                    1                    0   \n",
       "17           0                   0                    1                    0   \n",
       "22           0                   0                    1                    0   \n",
       "24           0                   0                    1                    0   \n",
       "\n",
       "    Offers Electives_YES  Mental Health Services_False  \\\n",
       "1                      1                             0   \n",
       "3                      1                             0   \n",
       "17                     1                             1   \n",
       "22                     1                             1   \n",
       "24                     1                             1   \n",
       "\n",
       "    Mental Health Services_True  AP Classes_NO  AP Classes_YES  \n",
       "1                             1              0               1  \n",
       "3                             1              0               1  \n",
       "17                            0              0               1  \n",
       "22                            0              0               1  \n",
       "24                            0              0               1  \n",
       "\n",
       "[5 rows x 194 columns]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dt_cleaned.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c8141e4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Final data set size: (166, 194)\n"
     ]
    }
   ],
   "source": [
    "# Export cleaned and transformed data to a new CSV file\n",
    "dt_cleaned.to_csv('cleaned_transformed_data.csv', index=False)\n",
    "\n",
    "# Print final data size and dimensions\n",
    "print(\"Final data set size:\", dt_cleaned.shape)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
