import pandas as pd
from sqlalchemy import create_engine #creates our db engine
from dotenv import load_dotenv #lets us read from our .env file

engine = create_engine(
    "postgresql+psycopg2://postgres@localhost:5432/postgres"
)

#we can execute raw sql queries using the execute method on our engine
query = "SELECT student_id, first_name, last_name, major FROM student;"
students_df = pd.read_sql(query, engine)

print(students_df)

#Create a new student in our db
new_student = pd.DataFrame({
    "first_name": ["Jaydan"],
    "last_name": ["Miller"],
    "email": ["jaydan.miller@email.com"],
    "major": ["CS"]
})

#the to_sql method allows us to write a dataframe to a sql table
new_student.to_sql(name = "student", con=engine, if_exists="append", index=False)

#we can update existing records 
update_sql = """
UPDATE student
SET major = 'DS'
WHERE email = 'jordan.miller@email.com';
"""
#update statements need to be executed using a connection
with engine.connect() as connection:
    connection.execute(update_sql)

#Delete records
delete_sql = """
DELETE FROM student
WHERE email = 'jordan.miller@email.com';
"""
with engine.connect() as connection:
    connection.execute(delete_sql)

#Call our stored procedure to get course count for student
student_id = 1
course_count_sql = f"""
CALL get_course_count_({student_id});
"""
course_count_df = pd.read_sql(course_count_sql, engine)
print(course_count_df)