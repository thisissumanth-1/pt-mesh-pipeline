import requests
from lxml import html
def scrape_website_info_xpath_with_headers(url):
    # Send an HTTP GET request with headers
    extracted_data = {}
    try:
        time.sleep(2)
        response = requests.get(url, headers=headers,timeout=30)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page using lxml
            page_content = html.fromstring(response.content)
            print(f"Important Information from {url}:\n")
            # Use XPath to extract titles
            if url == websites[0]:
                title = page_content.xpath("//title/text()")
                print(title)

                content_titles = page_content.xpath("//td//h3//text()")
                for heading in content_titles:
                    print("heading:", heading)

                # Extract and print image source URLs
                images = page_content.xpath("//td//img//@src")
                for image in images:
                    print("image:", image)

                # Extract and print dashboard links
                dashboard_links = page_content.xpath("//td//h4//a//@href")
                for link in dashboard_links:
                    print("dashboard_link:", link)

                # Extract and print subheadings
                subheadings = page_content.xpath("//td//p/text()")
                for subheading in subheadings:
                    print("subheading:", subheading)
                # Extract and print description text

                description = page_content.xpath(
                    "//div[contains(@class,'field-content')]//p//text()"
                )
                for text in description:
                    print("desctiption:", text)

            elif url == websites[1]:  # Specific logic for the second website
                titles = page_content.xpath("//title/text()")
                new_tenders_data = "".join(
                    page_content.xpath(
                        '//ul[contains(@class,"ui-list ui-list-m ui-list-news")]//li[1]//text()'
                    )
                ).strip()
                tender_changes_data = "".join(
                    page_content.xpath(
                        '//ul[contains(@class,"ui-list ui-list-m ui-list-news")]//li[2]//text()'
                    )
                ).strip()
                evaluation_results = "".join(
                    page_content.xpath(
                        '//ul[contains(@class,"ui-list ui-list-m ui-list-news")]//li[3]//text()'
                    )
                ).strip()
                all_data = "\n".join(
                    page_content.xpath(
                        "//div[contains(@class,'ui-list-div')][1]//ul[1]//li//a//text()"
                    )
                ).strip()

                print("Titles:", titles)
                print("New Tenders Data:", new_tenders_data)
                print("Tender Changes Data:", tender_changes_data)
                print("Evaluation Results:", evaluation_results)
                print("All Data:", all_data)

            elif url == websites[2]:
                titles = page_content.xpath("//title/text()")
                print("Title:", titles)

                policies = page_content.xpath(
                    "//div[contains(@class,'lunbo_tw')]//li//a//font//text()"
                )

                for policy in policies:
                    policy_data = policy
                    print("policy_data: ", policy_data)
                    
                transaction_announcement_data = page_content.xpath(
                    "//div[contains(@class,'main_list_on')]//li//a//font//text()"
                )

                for transaction in transaction_announcement_data:
                    transaction_data = transaction
                    print("transction_data: ", transaction_data)

            elif url == websites[3]:
                titles = page_content.xpath("//title/text()")
                new_tenders = page_content.xpath(
                    '//div[contains(@class,"w360 h286 fr")]//ul//a//text()'
                )
                for new_title in new_tenders:
                    print("new_tenders", new_title)

                tender_changes = page_content.xpath(
                    '//div[contains(@class,"w360 h286 fl")]//ul//a//text()'
                )
                for ten_title in tender_changes:
                    print("tender_changes_data", ten_title)

            elif url == websites[6]:
                titles = page_content.xpath("//title/text()")
                tender_tiles = page_content.xpath(
                    '//div[contains(@id,"vmarquee")]//table[contains(@id,"activeTenders")]//tr//a//text()'
                )
                for title in tender_tiles:
                    print("tender_titles", title)
                corrigendum_title = page_content.xpath(
                    "//tr[5]//table[contains(@class,'list_table')]//tr//a//text()"
                )
                for title_c in corrigendum_title:
                    print("corrigendum_title", title_c)
            else:
                titles = page_content.xpath("//title/text()")
                print("Title:", titles)
                h2_tags = page_content.xpath("//h2/text()")
                for h2 in h2_tags:
                    print("H2:", h2)

            print("\n" + "=" * 50 + "\n")  # Add a separator between websites
            return extracted_data
        else:
            print(
                f"Failed to retrieve the web page from {url}. Status code:",
                response.status_code,
            )
    except requests.exceptions.Timeout:
        print(f"Timeout error occurred while accessing {url}. Skipping this URL.")
    return None
