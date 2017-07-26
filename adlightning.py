import numpy as np

def main():

	try:
		csvFile = raw_input('Enter name of file: ')

		date,network_id,creative_id,dimensions,rp_preview_url,content,scanned,flash_content,flash_tracker,\
		video_auto,video_content,video_tracker,animation_frames,cpu_load,insecure_percent,network_requests,\
		network_size,tracking_pixels,preview_sequence,preview_static,edw_date,ext_creative_id,network_id,\
		network_name,size_id,short_name,rtb_seat_id,seat_name,advertiser_id,advertiser_name,number_of_combinations,\
		rtb_impressions,pub_gross_rev = np.genfromtxt(csvFile, delimiter = ',', unpack = True, dtype = 'str')

		filteredFile = open('filteredFile.csv', 'a')
		filteredData = ''

		headers = "date" +','+ "network_id" +','+ "creative_id" +','+ "dimensions" +','+ "rp_preview_url" +','+ "content" +','+ "scanned" +','+ "flash_content" +','+ "flash_tracker" +','+ \
		"video_auto" +','+ "video_content" +','+ "video_tracker" +','+ "animation_frames" +','+ "cpu_load" +','+ "insecure_percent" +','+ "network_requests" +','+ \
		"network_size" +','+ "tracking_pixels" +','+ "preview_sequence" +','+ "preview_static" +','+ "edw_date" +','+ "ext_creative_id" +','+ "network_id" +','+ \
		"network_name" +','+ "size_id" +','+ "short_name" +','+ "rtb_seat_id" +','+ "seat_name" +','+ "advertiser_id" +','+ "advertiser_name" +','+ "number_of_combinations" +','+ \
		"rtb_impressions" +','+ "pub_gross_rev" + '\n'

		filteredFile.write(headers)

		x = 0
		while x != len(date):
			if flash_content[x] == 'TRUE' and video_content[x] == 'TRUE':
				newLine = ''
				for item in date[x],network_id[x],creative_id[x],dimensions[x],rp_preview_url[x],content[x],scanned[x],flash_content[x],flash_tracker[x],\
				video_auto[x],video_content[x],video_tracker[x],animation_frames[x],cpu_load[x],insecure_percent[x],network_requests[x],\
				network_size[x],tracking_pixels[x],preview_sequence[x],preview_static[x],edw_date[x],ext_creative_id[x],network_id[x],\
				network_name[x],size_id[x],short_name[x],rtb_seat_id[x],seat_name[x],advertiser_id[x],advertiser_name[x],number_of_combinations[x],\
				rtb_impressions[x],pub_gross_rev[x]:
					newLine += item + ','
				filteredFile.write(newLine + '\n')
				x += 1

			else:
				x += 1

		filteredFile.close()
		print 'Script executed successfully.'

	except Exception, e:
		print str(e)

main()