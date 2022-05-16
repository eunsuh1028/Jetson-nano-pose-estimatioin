  if j == dis_list.index(sort_dis_list[0]) and exercise == 'BarbellSquat':
            inner_angle1, inner_angle2 = None, None
            try:
                # 왼쪽 허리 무릎 발  -> 엉덩이 무릎 발
                a = np.array(list(points[23]))
                b = np.array(list(points[25]))
                c = np.array(list(points[27]))

                # create vectors
                ba = a - b
                bc = c - b
                # calculate angle
                cosine_angle1 = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
                angle1 = np.arccos(cosine_angle1)
                inner_angle1 = np.degrees(angle1)
            except TypeError or UnboundLocalError:
                pass
            try:
                # 오른쪽 허리 무릎 발 -> 엉덩이 무릎 발
                d = np.array(list(points[24]))
                e = np.array(list(points[26]))
                f = np.array(list(points[28]))

                # create vectors
                ed = d - e
                ef = f - e
                # calculate angle
                cosine_angle2 = np.dot(ed, ef) / (np.linalg.norm(ed) * np.linalg.norm(ef))
                angle2 = np.arccos(cosine_angle2)
                inner_angle2 = np.degrees(angle2)
            except TypeError:
                pass
            Squat_score_flag1 = Squat_Before_flag

            if inner_angle1 != None and inner_angle2 == None:
                if inner_angle1 < 100:
                    status = 'Down'
                    Squat_Before_flag = True
                elif 100 <= inner_angle1 and inner_angle1 <= 120:
                    status = status
                    Squat_Before_flag = Squat_Before_flag
                elif inner_angle1 >= 120:
                    status = 'Up'
                    Squat_Before_flag = False
            elif inner_angle2 != None and inner_angle1 == None:
                if inner_angle2 < 100:
                    status = 'Down'
                    Squat_Before_flag = True
                elif 100 <= inner_angle2 and inner_angle2 <= 120:
                    pass
                elif inner_angle2 >= 120:
                    status = status
                    Squat_Before_flag = Squat_Before_flag
            elif inner_angle1 == None and inner_angle2 == None:
                pass
            else:
                if inner_angle2 < 100 or inner_angle1 < 100:
                    status = 'Down'
                    Squat_Before_flag = True
                elif (100 <= inner_angle2 and inner_angle2 <= 120) or (100 <= inner_angle1 and inner_angle1 <= 120):
                    status = status
                    Squat_Before_flag = Squat_Before_flag
                elif inner_angle2 >= 120 or inner_angle1 >= 120:
                    status = 'Up'
                    Squat_Before_flag = False
            Squat_score_flag2 = Squat_Before_flag

            if Squat_score_flag1 == True and Squat_score_flag2 == False:
                Squat_score += 1
                
                **********************************************************

        elif j == dis_list.index(sort_dis_list[0]) and exercise == 'BenchPress':
            inner_angle1, inner_angle2 = None, None
            try:
                a = np.array(list(points[15]))
                b = np.array(list(points[13]))
                c = np.array(list(points[11]))

                # create vectors
                ba = a - b
                bc = c - b
                # calculate angle
                cosine_angle1 = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
                angle1 = np.arccos(cosine_angle1)
                inner_angle1 = np.degrees(angle1)
            except TypeError or UnboundLocalError:
                pass

            try:
                d = np.array(list(points[16]))
                e = np.array(list(points[14]))
                f = np.array(list(points[12]))

                # create vectors
                ed = d - e
                ef = f - e
                # calculate angle
                cosine_angle2 = np.dot(ed, ef) / (np.linalg.norm(ed) * np.linalg.norm(ef))
                angle2 = np.arccos(cosine_angle2)
                inner_angle2 = np.degrees(angle2)
            except TypeError:
                pass

            Bench_score_flag1 = Bench_Before_flag
            if inner_angle1 != None and inner_angle2 == None:
                if inner_angle1 < 100:
                    bench_status = 'Down'
                    Bench_Before_flag = True
                elif 100 <= inner_angle1 and inner_angle1 <= 120:
                    bench_status = bench_status
                    Bench_Before_flag = Bench_Before_flag
                elif inner_angle1 >= 120:
                    bench_status = 'Up'
                    Dead_Before_flag = False
            elif inner_angle2 != None and inner_angle1 == None:
                if inner_angle2 < 100:
                    bench_status = 'Down'
                    Bench_Before_flag = True
                elif 100 <= inner_angle2 and inner_angle2 <= 120:
                    pass
                elif inner_angle2 >= 120:
                    bench_status = bench_status
                    Bench_Before_flag = Bench_Before_flag
            elif inner_angle1 == None and inner_angle2 == None:
                pass
            else:
                if inner_angle2 < 100 or inner_angle1 < 100:
                    bench_status = 'Down'
                    Bench_Before_flag = True
                elif (100 <= inner_angle2 and inner_angle2 <= 120) or (100 <= inner_angle1 and inner_angle1 <= 120):
                    bench_status = bench_status
                    Bench_Before_flag = Bench_Before_flag
                elif inner_angle2 >= 120 or inner_angle1 >= 120:
                    bench_status = 'Up'
                    Bench_Before_flag = False
            Bench_score_flag2 = Bench_Before_flag

            if Bench_score_flag1 == True and Bench_score_flag2 == False:
                Bench_score += 1
                
  ***************************************
  
        elif j == dis_list.index(sort_dis_list[0]) and exercise == 'Deadlift':
            inner_angle1, inner_angle2 = None, None
            try:
                # 왼쪽 허리 무릎 발
                a = np.array(list(points[23]))
                b = np.array(list(points[25]))
                c = np.array(list(points[27]))

                # create vectors
                ba = a - b
                bc = c - b
                # calculate angle
                cosine_angle1 = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
                angle1 = np.arccos(cosine_angle1)
                inner_angle1 = np.degrees(angle1)
            except TypeError or UnboundLocalError:
                pass
            try:
                # 오른쪽 허리 무릎 발
                d = np.array(list(points[24]))
                e = np.array(list(points[26]))
                f = np.array(list(points[28]))

                # create vectors
                ed = d - e
                ef = f - e
                # calculate angle
                cosine_angle2 = np.dot(ed, ef) / (np.linalg.norm(ed) * np.linalg.norm(ef))
                angle2 = np.arccos(cosine_angle2)
                inner_angle2 = np.degrees(angle2)
            except TypeError:
                pass
            Dead_score_flag1 = Dead_Before_flag

            if inner_angle1 != None and inner_angle2 == None:
                if inner_angle1 < 100:
                    dead_status = 'Down'
                    Dead_Before_flag = True
                elif 100 <= inner_angle1 and inner_angle1 <= 120:
                    dead_status = dead_status
                    Dead_Before_flag = Dead_Before_flag
                elif inner_angle1 >= 120:
                    dead_status = 'Up'
                    Dead_Before_flag = False
            elif inner_angle2 != None and inner_angle1 == None:
                if inner_angle2 < 100:
                    dead_status = 'Down'
                    Dead_Before_flag = True
                elif 100 <= inner_angle2 and inner_angle2 <= 120:
                    pass
                elif inner_angle2 >= 120:
                    dead_status = dead_status
                    Dead_Before_flag = Dead_Before_flag
            elif inner_angle1 == None and inner_angle2 == None:
                pass
            else:
                if inner_angle2 < 100 or inner_angle1 < 100:
                    dead_status = 'Down'
                    Dead_Before_flag = True
                elif (100 <= inner_angle2 and inner_angle2 <= 120) or (100 <= inner_angle1 and inner_angle1 <= 120):
                    dead_status = dead_status
                    Dead_Before_flag = Dead_Before_flag
                elif inner_angle2 >= 120 or inner_angle1 >= 120:
                    dead_status = 'Up'
                    Dead_Before_flag = False
            Dead_score_flag2 = Dead_Before_flag

            if Dead_score_flag1 == True and Dead_score_flag2 == False:
                Dead_score += 1

        j+=1

    return canvas, Squat_score, Bench_score, Dead_score, Squat_Before_flag, Bench_Before_flag, Dead_Before_flag,\
           squat_status, bench_status, dead_status
