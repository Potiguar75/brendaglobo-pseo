import os
import shutil

output_dir = "dist"

# Pulisce completamente la cartella dist
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

software_list = [
    {"id": "hubspot", "name": "HubSpot", "category": "CRM & Sales Automation", "aff_link": "https://partnerstack.com/tracking?s=hubspot"},
    {"id": "semrush", "name": "SEMrush", "category": "SEO & Marketing", "aff_link": "https://partnerstack.com/tracking?s=semrush"},
    {"id": "getresponse", "name": "GetResponse", "category": "Email Automation", "aff_link": "https://getresponse.com/?a=tracking"},
    {"id": "notion", "name": "Notion", "category": "Workspace & Knowledge Base", "aff_link": "https://notion.so/?mkt=affiliate"},
    {"id": "mailchimp", "name": "Mailchimp", "category": "Email & Marketing CRM", "aff_link": "https://mailchimp.com/affiliates/"},
    {"id": "salesforce", "name": "Salesforce", "category": "Enterprise CRM", "aff_link": "https://salesforce.com/affiliate"},
    {"id": "zendesk", "name": "Zendesk", "category": "Customer Support", "aff_link": "https://zendesk.com/affiliate"},
    {"id": "slack", "name": "Slack", "category": "Team Communication", "aff_link": "https://slack.com/affiliate"},
    {"id": "zoom", "name": "Zoom", "category": "Video Conferencing", "aff_link": "https://zoom.us/affiliate"},
    {"id": "shopify", "name": "Shopify", "category": "E-commerce", "aff_link": "https://shopify.com/affiliate"},
    {"id": "wordpress", "name": "WordPress", "category": "CMS & Hosting", "aff_link": "https://wordpress.org/affiliate"},
    {"id": "asana", "name": "Asana", "category": "Project Management", "aff_link": "https://asana.com/affiliate"},
    {"id": "trello", "name": "Trello", "category": "Task Management", "aff_link": "https://trello.com/affiliate"},
    {"id": "monday", "name": "Monday.com", "category": "Work OS", "aff_link": "https://monday.com/affiliate"},
    {"id": "clickup", "name": "ClickUp", "category": "Project Management", "aff_link": "https://clickup.com/affiliate"},
    {"id": "airtable", "name": "Airtable", "category": "Database & Workflow", "aff_link": "https://airtable.com/affiliate"},
    {"id": "activecampaign", "name": "ActiveCampaign", "category": "Marketing Automation", "aff_link": "https://activecampaign.com/affiliate"},
    {"id": "brevo", "name": "Brevo", "category": "Email & SMS Marketing", "aff_link": "https://brevo.com/affiliate"},
    {"id": "klaviyo", "name": "Klaviyo", "category": "E-commerce Marketing", "aff_link": "https://klaviyo.com/affiliate"},
    {"id": "stripe", "name": "Stripe", "category": "Payment Processing", "aff_link": "https://stripe.com/affiliate"},
    {"id": "quickbooks", "name": "QuickBooks", "category": "Accounting", "aff_link": "https://quickbooks.com/affiliate"},
    {"id": "xero", "name": "Xero", "category": "Accounting", "aff_link": "https://xero.com/affiliate"},
    {"id": "gusto", "name": "Gusto", "category": "Payroll & HR", "aff_link": "https://gusto.com/affiliate"},
    {"id": "buffer", "name": "Buffer", "category": "Social Media Management", "aff_link": "https://buffer.com/affiliate"},
    {"id": "canva", "name": "Canva", "category": "Graphic Design", "aff_link": "https://canva.com/affiliate"},
    {"id": "figma", "name": "Figma", "category": "UI/UX Design", "aff_link": "https://figma.com/affiliate"},
    {"id": "loom", "name": "Loom", "category": "Video Messaging", "aff_link": "https://loom.com/affiliate"},
    {"id": "miro", "name": "Miro", "category": "Visual Collaboration", "aff_link": "https://miro.com/affiliate"},
    {"id": "dropbox", "name": "Dropbox", "category": "Cloud Storage", "aff_link": "https://dropbox.com/affiliate"},
    {"id": "googleworkspace", "name": "Google Workspace", "category": "Office Suite", "aff_link": "https://workspace.google.com/affiliate"},
    {"id": "microsoft365", "name": "Microsoft 365", "category": "Productivity Suite", "aff_link": "https://microsoft.com/affiliate"},
    {"id": "jira", "name": "Jira", "category": "Issue Tracking", "aff_link": "https://atlassian.com/software/jira"},
    {"id": "confluence", "name": "Confluence", "category": "Documentation", "aff_link": "https://atlassian.com/software/confluence"},
    {"id": "github", "name": "GitHub", "category": "Code Hosting", "aff_link": "https://github.com"},
    {"id": "gitlab", "name": "GitLab", "category": "DevOps Platform", "aff_link": "https://about.gitlab.com"},
    {"id": "intercom", "name": "Intercom", "category": "Customer Messaging", "aff_link": "https://intercom.com"},
    {"id": "drift", "name": "Drift", "category": "Conversational Marketing", "aff_link": "https://drift.com"},
    {"id": "typeform", "name": "Typeform", "category": "Forms & Surveys", "aff_link": "https://typeform.com"},
    {"id": "calendly", "name": "Calendly", "category": "Scheduling", "aff_link": "https://calendly.com"},
    {"id": "docusign", "name": "DocuSign", "category": "E-Signatures", "aff_link": "https://docusign.com"},
    {"id": "hotjar", "name": "Hotjar", "category": "Behavior Analytics", "aff_link": "https://hotjar.com"},
    {"id": "mixpanel", "name": "Mixpanel", "category": "Product Analytics", "aff_link": "https://mixpanel.com"},
    {"id": "segment", "name": "Segment", "category": "Customer Data Platform", "aff_link": "https://segment.com"},
    {"id": "tableau", "name": "Tableau", "category": "Business Intelligence", "aff_link": "https://tableau.com"},
    {"id": "powerbi", "name": "Power BI", "category": "Business Intelligence", "aff_link": "https://microsoft.com/power-bi"},
    {"id": "webflow", "name": "Webflow", "category": "Website Builder", "aff_link": "https://webflow.com"},
    {"id": "squarespace", "name": "Squarespace", "category": "Website Builder", "aff_link": "https://squarespace.com"},
    {"id": "wix", "name": "Wix", "category": "Website Builder", "aff_link": "https://wix.com"},
    {"id": "hootsuite", "name": "Hootsuite", "category": "Social Media Management", "aff_link": "https://hootsuite.com"},
    {"id": "sprout", "name": "Sprout Social", "category": "Social Media Management", "aff_link": "https://sproutsocial.com"}
]

os.makedirs(output_dir, exist_ok=True)

index_links = []
sitemap_urls = []
count = 0
base_url = "https://brendaglobo-pseo.geom-cmarco.workers.dev"

for i in range(len(software_list)):
    for j in range(len(software_list)):
        if i != j:
            sw_a = software_list[i]
            sw_b = software_list[j]
            
            filename = f"{sw_a['id']}-vs-{sw_b['id']}.html"
            filepath = os.path.join(output_dir, filename)
            index_links.append(f'<li><a href="{filename}">{sw_a["name"]} vs {sw_b["name"]} Comparison</a></li>')
            sitemap_urls.append(f"<url><loc>{base_url}/{filename}</loc><changefreq>weekly</changefreq></url>")
            
            html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{sw_a['name']} vs {sw_b['name']} | Enterprise Software Comparison</title>
    <meta name="description" content="Detailed comparison between {sw_a['name']} and {sw_b['name']} for global B2B infrastructure and workflows.">
</head>
<body style="font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; line-height: 1.6;">
    <p><a href="index.html">&larr; Back to all comparisons</a></p>
    <h1>{sw_a['name']} vs {sw_b['name']}</h1>
    <p>Looking for the optimal SaaS infrastructure setup? Here is how <strong>{sw_a['name']}</strong> and <strong>{sw_b['name']}</strong> compare across key enterprise metrics.</p>
    
    <h2>Key Overview</h2>
    <ul>
        <li><strong>{sw_a['name']} Category:</strong> {sw_a['category']}</li>
        <li><strong>{sw_b['name']} Category:</strong> {sw_b['category']}</li>
    </ul>
    
    <div style="margin-top: 40px; padding: 20px; background: #f9f9f9; border-radius: 8px;">
        <h3>Ready to choose?</h3>
        <p>Explore official plans and current offers:</p>
        <a href="{sw_a['aff_link']}?utm_source=pseo&utm_medium=comparison&utm_campaign={sw_a['id']}-vs-{sw_b['id']}" target="_blank" rel="sponsored noopener noreferrer" style="display: inline-block; padding: 12px 24px; background: #0052cc; color: #fff; text-decoration: none; border-radius: 4px; font-weight: bold;">Check {sw_a['name']}</a>
        <a href="{sw_b['aff_link']}?utm_source=pseo&utm_medium=comparison&utm_campaign={sw_a['id']}-vs-{sw_b['id']}" target="_blank" rel="sponsored noopener noreferrer" style="display: inline-block; padding: 12px 24px; background: #4a5568; color: #fff; text-decoration: none; border-radius: 4px; font-weight: bold; margin-left: 10px;">Check {sw_b['name']}</a>
    </div>
</body>
</html>"""

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html_content)
            count += 1

# Homepage (con Google Search Console verification tag)
links_html_str = "\n".join(index_links)
index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="-_QOXuXXhL7Ata7XDMemgIZfP4nrfa2VuAb9nuC7_Yc" />
    <title>BrendaGlobo | B2B Enterprise Software Comparisons</title>
</head>
<body style="font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; line-height: 1.6;">
    <h1>BrendaGlobo Software Comparisons</h1>
    <p>Automated infrastructure and tool comparisons for global B2B operations. Total active comparisons: {count}.</p>
    <ul>
        {links_html_str}
    </ul>
</body>
</html>"""

with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_content)

# Sitemap
sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url><loc>{base_url}/index.html</loc><changefreq>daily</changefreq></url>
    {"\n".join(sitemap_urls)}
</urlset>"""

with open(os.path.join(output_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_content)
