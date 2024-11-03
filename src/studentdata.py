from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

#new function to create a normalised database for the student enrollment data
def create_normalised_db(df):
    # Create the SQL statements to create the tables in the database.
    student_sql = '''CREATE TABLE IF NOT EXISTS student (
                        student_id INTEGER PRIMARY KEY,
                        student_name TEXT NOT NULL,
                        student_email TEXT NOT NULL);
                        '''
    teacher_sql = '''CREATE TABLE IF NOT EXISTS teacher (
                        teacher_id INTEGER PRIMARY KEY,
                        teacher_name TEXT NOT NULL,
                        teacher_email TEXT NOT NULL);
                        '''
    course_sql = '''CREATE TABLE IF NOT EXISTS course (
                        course_id INTEGER PRIMARY KEY,
                        course_name TEXT NOT NULL,
                        course_description TEXT NOT NULL);
                        '''
    enrollment_sql = '''CREATE TABLE IF NOT EXISTS enrollment (
                            student_id INTEGER NOT NULL, 
                            course_id INTEGER NOT NULL,
                            teacher_id INTEGER,
                            PRIMARY KEY (student_id, course_id, teacher_id),
                            FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id) ON UPDATE CASCADE ON DELETE SET NULL);
                            '''
    
    # Create a connection to the database using sqlite3.
    db_path = project_root.joinpath('tutorialpkg', 'data_db_activity', 'enrollments_normalised.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreign_keys = ON;')
    cursor.execute(student_sql)
    cursor.execute(teacher_sql)
    cursor.execute(course_sql)
    #cursor.execute(enrollment_sql)

    # Insert the data into the tables.
    df_students = df[['student_name', 'student_email']].drop_duplicates()
    df_students.to_sql('student', conn, if_exists='replace', index=False)
    df_teachers = df[['teacher_name', 'teacher_email']].drop_duplicates()
    df_teachers.to_sql('teacher', conn, if_exists='replace', index=False)
    df_courses = df[['course_id','course_name', 'course_description']].drop_duplicates()
    df_courses.to_sql('course', conn, if_exists='replace', index=False)
    df_enrollments = df[['student_id', 'course_id', 'teacher_id']].drop_duplicates()
    df_enrollments.to_sql('enrollment', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

if __name__ == '__main__':                  
    project_root = Path(__file__).parent
    csv_file = project_root.joinpath('tutorialpkg', 'data_db_activity', 'student_data.csv')
    df = pd.read_csv(csv_file)
    
    # Create a connection to the database using sqlite3.
    #db_path = project_root.joinpath('tutorialpkg', 'data_db_activity', 'enrollments_unnormalised.db')
    #conn = sqlite3.connect(db_path)
    # Save the dataframe to the database, this will create a table called 'enrollments' and replace it if
    # it exists. The index column is not saved to the table.
    # If the file does not exist then it will be created.
    #df.to_sql('enrollments', conn, if_exists='replace', index=False)

    #conn.close()
    create_normalised_db(df)