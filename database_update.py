from config import connection

connection.autocommit = True

def database_update(curr_week):
    if curr_week % 2 == 0:
        try:
             with connection.cursor() as cursor:
                    cursor.execute("""
                    UPDATE days.monday 
                    SET subject='Вычислительная техника лаб.'
                    WHERE id=2;
                    """)
                    cursor.execute("""
                    UPDATE days.monday 
                    SET subject='Физическая культура', teacher='Горячева Н.Н.'
                    WHERE id=3;
                    """)
                    cursor.execute("""
                    UPDATE days.monday 
                    SET subject='Физическая культура', teacher='Горячева Н.Н.'
                    WHERE id=3;
                    """)
                    cursor.execute("""
                                UPDATE days.wednesday 
                                SET subject='Вычислительная техника лаб.', teacher='Изотова А.А.', room='314'
                                WHERE id=2;
                                """)
                    cursor.execute("""
                                UPDATE days.wednesday 
                                SET subject='Информационная экология лаб', teacher='Курбатов В.А.', room='339'
                                WHERE id=3;
                                """)
                    cursor.execute("""
                                UPDATE days.wednesday 
                                SET subject='Введение в ИТ лаб.', teacher='Мкртчян Г.М.', room='ВЦ127'
                                WHERE id=4;
                                """)
                    cursor.execute("""
                                UPDATE days.wednesday 
                                SET subject='Введение в ИТ лаб.', teacher='Мкртчян Г.М.', room='ВЦ127'
                                WHERE id=5;
                                """)
                    cursor.execute("""
                                UPDATE days.thursday 
                                SET subject='Информационная экология лек', teacher='Курбатов В.А.', room='дист'
                                WHERE id=1;
                                """)
                    cursor.execute("""
                                UPDATE days.thursday 
                                SET subject='Компьютерная графика лек', teacher='Рывлина А.А..', room='дист'
                                WHERE id=3;
                                """)
                    cursor.execute("""
                                UPDATE days.saturday
                                SET subject='Введение в ИТ пр.з.', teacher='Мкртчян Г.М.', room='дист'
                                WHERE id=3;
                                """)
                    cursor.execute("""
                                UPDATE days.saturday
                                SET subject='Введение в ИТ пр.з.', teacher='Мкртчян Г.М.', room='дист'
                                WHERE id=4;
                                """)
        except Exception as _ex:
                print('Update error is ', _ex)
    else:
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE days.monday 
                    SET subject='Вычислительная техника пр.з..'
                    WHERE id=2;
                    """)
                cursor.execute("""
                    UPDATE days.monday 
                    SET subject='Иностранный язык пр.з.', teacher = 'Анна Юрьевна'
                    WHERE id=3;
                    """)
                cursor.execute("""
                    UPDATE days.wednesday 
                    SET subject='Алгебра и геометрия лек.', teacher='Куприн А.В', room='дист'
                    WHERE id=2;
                    """)
                cursor.execute("""
                    UPDATE days.wednesday 
                    SET subject='Введение в ИТ лек.', teacher='Доткулова А.В.', room='дист'
                    WHERE id=3;
                    """)
                cursor.execute("""
                                DELETE FROM days.wednesday WHERE id=4
                                """)
                cursor.execute("""
                                DELETE FROM days.wednesday WHERE id=5
                                """)
                cursor.execute("""
                                UPDATE days.thursday 
                                SET subject='Философия лек.', teacher='Глинский А.В.', room='дист'
                                WHERE id=1;
                                """)
                cursor.execute("""
                                DELETE FROM days.thursday  WHERE id=3
                                """)
                cursor.execute("""
                                DELETE FROM days.saturday WHERE id=3
                                """)
                cursor.execute("""
                                DELETE FROM days.saturday WHERE id=3
                                """)
        except Exception as _ex:
            print('Error is', _ex)