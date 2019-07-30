insert_new_status = " INSERT INTO StatusData (HOSTNAME , DATA) VALUES('{HOSTNAME}','{DATA}')"

get_latest_status = """
                    SELECT DATA FROM STATUSDATA WHERE HOSTNAME = '{HOSTNAME}' order by TS DESC LIMIT 1
                    """