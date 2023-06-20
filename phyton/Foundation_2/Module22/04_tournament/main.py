tour_file = open('first_tour.txt', 'r')
tour2_file = open('second_tour.txt', 'w')
win_score = int(tour_file.readline().replace('\n',''))
win_people = sorted([[s_elem.split()[2], '{}. {}'.format(s_elem.split()[1][0], s_elem.split()[0])]
                     for s_elem in tour_file
                     if int(s_elem.split()[2]) > win_score], reverse=True)
tour2_file.write(str(len(win_people))+'\n')
tour2_file.writelines(['{}) {} {}\n'.format(int(i+1), win_people[i][1], str(win_people[i][0])) for i in range(len(win_people))])
tour_file.close()
tour2_file.close()