import streamlit as st

def get_job_description():
    # Define job roles and descriptions
    job_descriptions = {
        "Software Engineer": "As a Software Engineer, you will be responsible for developing, testing, and maintaining software applications that meet the business needs of the organization. You will work closely with cross-functional teams including product managers, designers, and other engineers to build scalable and reliable systems. Your duties will include writing clean, efficient code, debugging and troubleshooting software issues, and ensuring applications run smoothly across different platforms. In this role, a strong understanding of programming languages, software development methodologies, and problem-solving skills is essential. You will also be responsible for code reviews, collaborating on system architecture, and improving the overall software development lifecycle. Excellent communication skills, a passion for technology, and the ability to work in a fast-paced environment are key to success in this role",
        "Data Acientist": "As a Data Scientist, you will analyze complex data sets to uncover insights that drive business decisions. Your role involves using statistical methods, machine learning models, and advanced analytics to interpret data and present findings to stakeholders in a clear and actionable manner. You will collaborate with teams across the organization to implement data-driven solutions that optimize processes, improve customer experiences, and generate business value. Proficiency in programming languages such as Python, R, or SQL, and a deep understanding of statistical analysis, data visualization, and machine learning algorithms will be crucial. Additionally, your ability to communicate technical findings to non-technical stakeholders will be important for aligning data solutions with business objectives",
        "Product manager": "As a Product Manager, you will be the driving force behind the development and delivery of products that meet the needs of customers and align with the company’s business goals. Your primary responsibility is to define the product roadmap, prioritize features, and ensure timely delivery of high-quality products. You will work with cross-functional teams, including engineering, marketing, sales, and design, to gather requirements, manage timelines, and launch successful products. Excellent communication, leadership, and decision-making skills are critical, as you will be required to communicate product vision, track product performance, and make strategic decisions based on market feedback. A deep understanding of market trends, customer needs, and competitive analysis will help you guide the product lifecycle from ideation to launch and beyond.",
        "Project Manager": "As a Project Manager, you will oversee the planning, execution, and delivery of projects across multiple teams. Your role will involve managing resources, defining project scope, setting deadlines, and ensuring that projects are completed on time, within budget, and to the highest quality standards. You will collaborate with stakeholders to define project goals and milestones, while mitigating risks and resolving issues that may arise during the project lifecycle. Strong organizational, communication, and leadership skills are essential, as you will be managing a variety of teams and ensuring seamless coordination between all parties involved. Your ability to adapt to changing requirements, prioritize tasks, and drive the project to successful completion is key to achieving project goals.",
        "Business Analyst": "As a Business Analyst, you will act as a bridge between business stakeholders and technical teams, ensuring that business needs are accurately captured and translated into technical requirements. Your role will involve gathering and analyzing data to identify areas for improvement and opportunities to streamline business operations. You will document business processes, assess system performance, and support decision-making by providing actionable insights and recommendations. Strong analytical skills, an ability to understand business workflows, and proficiency in data visualization and reporting tools are critical in this role. Effective communication and the ability to work with various departments to implement solutions will ensure that the company remains competitive and efficient in its operations.",
        "Machine learning Engineer": "As a Machine Learning Engineer, you will design, develop, and deploy machine learning models that automate processes, generate insights, and optimize business outcomes. Your role will involve working with large data sets, implementing algorithms, and using statistical and computational techniques to build models that can learn from data and make predictions. You will collaborate with data scientists, software engineers, and other stakeholders to integrate machine learning models into existing applications or systems. Proficiency in machine learning libraries such as TensorFlow, PyTorch, and scikit-learn, as well as a strong background in programming (especially Python), will be essential. You will also be responsible for evaluating model performance, tuning algorithms, and ensuring that the models are scalable and efficient for real-world applications. Strong problem-solving abilities and a deep understanding of both theoretical and practical machine learning concepts will be crucial in this role.",
        "Marketing Manager": "As a Marketing Manager, you will oversee the development and execution of marketing strategies that promote the company’s products or services and drive brand awareness. You will be responsible for managing marketing campaigns, analyzing market trends, conducting competitor analysis, and identifying customer needs to create targeted marketing efforts. Your duties will include leading a team of marketing professionals, working with creative teams to produce compelling content, managing the marketing budget, and measuring the effectiveness of campaigns. Strong communication skills, creativity, and a data-driven approach to marketing are essential for this role. A deep understanding of digital marketing channels, SEO, social media, and email marketing will be key to driving successful initiatives.",
        "Sales Manager": "As a Sales Manager, you will lead a team of sales professionals to drive revenue and achieve sales targets. Your role will involve setting sales goals, creating sales strategies, and motivating your team to meet and exceed objectives. You will be responsible for identifying potential business opportunities, developing relationships with new and existing clients, and negotiating contracts. In addition, you will analyze sales data, forecast future sales trends, and collaborate with marketing teams to align sales campaigns with market demands. Excellent leadership, negotiation, and interpersonal skills, along with a thorough understanding of the sales cycle, are crucial for success in this role. You will also play a key role in managing customer relationships to ensure long-term business growth.",
        "HR Manager": "As an HR Manager, you will manage all aspects of human resources within the company, focusing on recruitment, employee development, performance management, and organizational culture. You will be responsible for developing and implementing HR policies, handling employee relations, ensuring compliance with labor laws, and overseeing compensation and benefits programs. Your role will include collaborating with management to assess staffing needs, conducting interviews, onboarding new employees, and facilitating training and development programs. Strong interpersonal skills, leadership, and the ability to manage complex employee situations are essential. Additionally, a deep understanding of HR software, labor laws, and best practices in talent management will help you effectively support both employees and leadership.",
        "Financial Analyst": "As a Financial Analyst, you will be responsible for analyzing financial data, preparing reports, and providing insights to guide the company’s financial decision-making. Your role will involve conducting budgeting and forecasting, analyzing financial performance, and helping to identify areas for cost optimization. You will work closely with various departments to provide financial advice on investments, revenue growth, and cost management. You will also monitor market trends and economic conditions to evaluate their impact on the company’s finances. Proficiency in financial modeling, accounting principles, and Excel is essential. Strong analytical and problem-solving skills, as well as the ability to communicate complex financial information to non-financial stakeholders, are key to success in this role.",
        "Operations Manager":"As an Operations Manager, you will be responsible for overseeing the daily operations of the company to ensure efficiency, productivity, and the smooth running of business processes. Your role will involve managing workflows, optimizing resources, and working with department heads to improve operational systems. You will be responsible for ensuring that operations meet quality standards, coordinating with supply chain management, and managing inventory and logistics. Additionally, you will analyze operational performance metrics, implement process improvements, and handle budget planning for operations. Strong leadership, organizational skills, and the ability to solve operational problems quickly will be essential. A background in project management and experience with process automation and optimization tools will help you succeed in this role.",
        "Software Developer":"As a Software Developer, you will be responsible for designing, coding, and testing software applications to meet the needs of the company and its users. Your role will involve collaborating with product managers, designers, and other developers to create robust, scalable, and efficient software solutions. You will write clean, maintainable code and ensure that software meets user requirements and functional specifications. Additionally, you will troubleshoot and debug software issues, perform unit testing, and ensure code quality through code reviews and collaboration with peers. A strong understanding of programming languages such as Java, Python, C++, or JavaScript, as well as knowledge of software development methodologies, is essential for this role. Your ability to work in a team environment and adapt to changing technologies will be key to your success.",
        "Cloud Engineer":"As a Cloud Engineer, you will be responsible for the design, implementation, and maintenance of cloud infrastructure and services to support the company’s applications and data storage needs. Your role will involve working with cloud platforms such as AWS, Microsoft Azure, or Google Cloud to build scalable and secure cloud solutions. You will collaborate with software engineers to ensure that applications are deployed effectively on the cloud, manage cloud resources efficiently, and monitor the performance of cloud-based systems. Strong knowledge of cloud computing principles, infrastructure automation tools (like Terraform or Ansible), and cloud security best practices will be crucial for this role. You will also be tasked with optimizing cloud costs, ensuring high availability, and providing solutions to improve performance.",
        "Cybersecurity Analyst":"As a Cybersecurity Analyst, you will be responsible for protecting the company’s networks, systems, and data from security breaches and cyber threats. Your role will involve monitoring network traffic, identifying vulnerabilities, conducting security assessments, and responding to incidents such as data breaches or malware attacks. You will collaborate with IT teams to implement security protocols, recommend best practices, and ensure compliance with industry standards and regulations. Strong knowledge of security tools and technologies, including firewalls, intrusion detection systems (IDS), and encryption, is essential. Your ability to stay ahead of emerging threats, analyze security logs, and communicate security risks to both technical and non-technical stakeholders will be key to the company’s security posture.",
        "Systems Administrator":"As a Systems Administrator, you will manage and maintain the company’s IT infrastructure, ensuring the efficient operation of servers, networks, and other critical systems. You will be responsible for installing, configuring, and troubleshooting hardware and software, as well as performing regular system updates and backups. Your role will also include monitoring system performance, ensuring security policies are enforced, and providing technical support to end-users. A solid understanding of operating systems (Windows, Linux, etc.), networking, virtualization, and system security is crucial. You will also be tasked with managing user accounts, resolving hardware and software issues, and automating system administration tasks to improve operational efficiency.",
        "UI/UX Designer":"As a UI/UX Designer, you will be responsible for designing intuitive and engaging user interfaces and enhancing user experiences across various digital products. Your role will involve collaborating with product managers, developers, and other stakeholders to create wireframes, prototypes, and high-fidelity designs for web and mobile applications. You will conduct user research, usability testing, and analyze user feedback to ensure that designs are user-centered and meet business goals. Strong knowledge of design tools such as Adobe XD, Sketch, or Figma, along with an understanding of design principles, accessibility, and responsive design, will be crucial for success. Your ability to balance aesthetics with functionality and ensure seamless user experiences will be key to the success of the product.",
        "Data Analyst":"As a Data Analyst, you will be responsible for interpreting complex data to provide actionable insights that help drive business decisions. Your role involves collecting, processing, and analyzing data from multiple sources to uncover trends and patterns. You will create visualizations and reports to present findings to stakeholders in a clear and actionable manner. Your work will also include designing and conducting surveys, interpreting statistical models, and performing data cleansing to ensure data quality. Proficiency in data analysis tools such as Excel, SQL, Python, or R, as well as experience with data visualization tools like Tableau or Power BI, is essential. Your ability to communicate insights and provide recommendations to non-technical stakeholders will be key to supporting data-driven decision-making across the organization.",
        "Web Developer":"As a Web Developer, you will be responsible for designing, coding, and maintaining websites and web applications that meet user needs and business goals. Your role will involve working with front-end technologies like HTML, CSS, JavaScript, and back-end technologies such as PHP, Node.js, or Python to build dynamic, responsive websites. You will collaborate with designers, product managers, and other developers to implement new features, fix bugs, and improve the user experience. Knowledge of version control systems like Git, familiarity with web development frameworks (e.g., React, Angular, or Django), and an understanding of responsive design are crucial for this role. Strong problem-solving skills, attention to detail, and the ability to work efficiently in a team will help you thrive in this role.",
        "Database Administrator":"As a Database Administrator (DBA), you will be responsible for the design, implementation, and maintenance of databases that support business applications and data storage needs. You will ensure that databases are secure, highly available, and efficiently optimized for performance. Your role will involve tasks such as database backups, recovery, troubleshooting, performance tuning, and ensuring compliance with data security standards. You will work closely with developers to optimize database queries and integrate database systems into the company’s infrastructure. Proficiency in SQL and experience with database management systems (DBMS) such as MySQL, PostgreSQL, or Microsoft SQL Server are essential for this role. Strong analytical skills, attention to detail, and a deep understanding of database architecture are key to success.",
        "IT Support Specialist":"As an IT Support Specialist, you will provide technical assistance and support to end-users, ensuring the smooth operation of hardware, software, and network systems. Your role will involve troubleshooting and resolving technical issues, installing and configuring new devices, managing software installations, and providing training to users. You will also assist in the maintenance of IT infrastructure, ensuring that systems are updated, secure, and functioning properly. Strong communication skills are essential as you will be the first point of contact for employees experiencing technical problems. Experience with operating systems (Windows, macOS, Linux), familiarity with helpdesk ticketing systems, and an understanding of basic networking principles will be crucial in this role. Your ability to work efficiently under pressure and provide timely solutions will contribute to maintaining a productive work environment.",
        "Network Engineer":"As a Network Engineer, you will be responsible for designing, implementing, and maintaining the company’s network infrastructure, ensuring that it is efficient, secure, and scalable. You will configure and troubleshoot network hardware, such as routers, switches, firewalls, and wireless access points, and ensure optimal network performance. Your role will involve monitoring network traffic, diagnosing network issues, and implementing solutions to improve reliability and speed. You will also work closely with security teams to protect the network from potential cyber threats and ensure compliance with industry standards. A strong understanding of networking protocols (TCP/IP, DNS, VPN, etc.), network security principles, and hands-on experience with network devices are essential for this role. Strong problem-solving skills, attention to detail, and the ability to work under pressure are key to succeeding in this role.",
        "Full Stack Developer":"As a Full Stack Developer, you will be responsible for developing both the front-end and back-end of web applications. You will work on creating seamless and efficient user interfaces using front-end technologies such as HTML, CSS, JavaScript, and frameworks like React or Angular. On the back-end, you will work with technologies like Node.js, Python, Ruby, or Java, and manage databases using MySQL, MongoDB, or PostgreSQL. Your role will involve building and maintaining the entire web application architecture, ensuring it is scalable, secure, and optimized for performance. You will collaborate with designers, product managers, and other developers to ensure that applications meet both user and business needs. Strong problem-solving skills, proficiency in full stack development tools, and experience with cloud platforms (AWS, Azure, etc.) are essential for this role.",
        "AI Engineer":"As an AI Engineer, you will be responsible for designing, developing, and implementing machine learning algorithms and models to solve business challenges. You will work on data preprocessing, training models, and evaluating their performance to ensure they are effective in making predictions or automating tasks. Your role will require strong knowledge of AI and machine learning techniques, such as supervised learning, unsupervised learning, reinforcement learning, and deep learning. You will collaborate with data scientists and software engineers to integrate AI models into applications and ensure that they scale effectively. Proficiency in programming languages like Python, R, and frameworks such as TensorFlow or PyTorch, along with experience in data manipulation and model optimization, is crucial. Your ability to stay updated with AI trends and apply new technologies will be key to your success.",
        "Mobile App Developer":"As a Mobile App Developer, you will design, develop, and maintain mobile applications for iOS and Android platforms. You will be responsible for ensuring that applications are user-friendly, efficient, and responsive across a wide range of mobile devices. Your role will involve working with native programming languages like Swift (for iOS) or Kotlin/Java (for Android), as well as cross-platform frameworks such as Flutter or React Native. You will collaborate with designers to create intuitive user interfaces and ensure that the app performs smoothly with minimal bugs. Additionally, you will be responsible for integrating APIs, managing data storage, and ensuring the app meets performance and security standards. Strong programming skills, familiarity with mobile development tools, and an understanding of mobile UI/UX principles will be essential for this role.",
        "Quality Assurance Engineer":"As a Quality Assurance (QA) Engineer, you will be responsible for ensuring the quality and functionality of the company’s software products. Your role will involve creating and executing test plans to identify software defects, running manual and automated tests, and working closely with developers to resolve issues. You will conduct functional, regression, and performance testing to ensure that applications meet the required standards and are free from critical bugs. You will also be responsible for documenting defects, creating test cases, and verifying bug fixes. A strong understanding of testing methodologies, experience with testing tools like Selenium, JUnit, or TestNG, and the ability to communicate defects and improvements clearly will be essential. Attention to detail, problem-solving skills, and the ability to work under deadlines will contribute to ensuring high-quality products.",
        "Business Development Manager":"As a Business Development Manager, you will be responsible for identifying new business opportunities, expanding market reach, and building long-term relationships with potential clients and partners. Your role will involve researching market trends, identifying new areas for growth, negotiating contracts, and developing strategies to increase sales and revenue. You will work closely with marketing, sales, and product teams to align business development efforts with organizational goals. Your tasks will include leading market expansion efforts, networking with key stakeholders, and developing partnerships that drive company growth. Strong communication, negotiation, and project management skills are essential for this role. Additionally, an understanding of market analysis, competitor research, and experience in relationship management will help you excel in achieving business growth.",
        "Digital Marketing Specialist":"A Digital Marketing Specialist is responsible for creating, implementing, and managing online marketing campaigns across various platforms. This role involves working with SEO, PPC, social media marketing, email campaigns, and content creation. The primary goal is to increase brand visibility, attract potential customers, and drive conversions. Digital Marketing Specialists must stay updated with the latest trends, algorithms, and digital tools to optimize campaigns. Strong analytical skills are needed to track the performance of campaigns, adjust strategies, and report results to stakeholders.",
        "Customer Support Manager":"The Customer Support Manager oversees a team that assists customers with inquiries, complaints, and technical issues. This role involves setting up support systems, training staff, developing FAQs, and ensuring customers receive prompt and professional service. Customer Support Managers also analyze customer feedback to identify areas for improvement, maintain customer satisfaction, and resolve any escalated issues. Excellent communication skills, problem-solving abilities, and experience with CRM software are essential for this role.",
        "Legal Counsel":"Legal Counsel provides legal advice and guidance to organizations to ensure that they comply with laws and regulations. Responsibilities include reviewing contracts, handling legal disputes, ensuring proper documentation, and mitigating legal risks. Legal Counsel may also represent the organization in court and work closely with external lawyers. A law degree, attention to detail, and the ability to communicate complex legal terms clearly are essential for this role.",
        "Content Writer":"Content Writers create written material for websites, blogs, social media, advertisements, and other marketing platforms. The role involves conducting research, writing compelling content that engages readers, and ensuring the content aligns with the brand's voice and goals. Content Writers must be proficient in SEO techniques to optimize content for search engines. Strong writing skills, creativity, and the ability to meet deadlines are key to success in this role.",
        "Graphic Designer":"A Graphic Designer is responsible for creating visual content for marketing, advertising, and branding. This includes designing logos, websites, social media posts, brochures, and advertisements. Graphic Designers work closely with marketing teams to ensure that their designs align with brand guidelines. Proficiency in design software such as Adobe Creative Suite, strong creativity, and a keen eye for detail are required for this role.",
        "Video Producer":"A Video Producer manages the creation of video content for marketing, training, or entertainment purposes. The role involves pre-production planning, directing, shooting, and editing videos. Video Producers work with other departments to understand the objectives of the video, manage the production timeline, and ensure that the final product is high-quality and meets the required standards. Creativity, technical skills in video editing software, and strong project management abilities are essential.",
        "SEO Specialist":"An SEO Specialist is responsible for optimizing website content and structure to rank higher on search engines. This involves keyword research, content optimization, on-page and off-page SEO, and technical SEO tasks. SEO Specialists analyze website analytics to monitor performance and identify opportunities for improvement. Strong understanding of search engine algorithms, SEO tools (like Google Analytics, SEMrush), and the ability to stay updated with SEO trends are essential for success in this role.",
        "Copywriter":"A Copywriter creates persuasive and engaging content designed to promote products, services, or brands. Responsibilities include writing advertising copy, product descriptions, landing page content, and email marketing campaigns. Copywriters work closely with marketing teams to ensure their content aligns with the brand’s messaging and goals. Creativity, strong writing skills, and an understanding of the target audience are essential for this role.",
        "Public Relations Manager":"A Public Relations (PR) Manager is responsible for managing a company’s public image and media relations. The role involves drafting press releases, organizing events, and maintaining relationships with journalists, influencers, and the public. PR Managers also work to resolve any negative publicity and shape the company’s communication strategy. Strong communication, crisis management, and media relations skills are crucial for this role.",
        "Event Coordinator":"An Event Coordinator plans and organizes events such as conferences, seminars, and corporate functions. The role involves selecting venues, managing event logistics, coordinating with vendors, and ensuring that the event runs smoothly. Event Coordinators also handle the marketing of events and attendee registration. Strong organizational skills, attention to detail, and the ability to multitask under pressure are essential for success in this role.",
        "Account Manager":"An Account Manager serves as the primary point of contact between clients and the company. The role involves managing client relationships, ensuring the timely delivery of services or products, and identifying opportunities for upselling or cross-selling. Account Managers are responsible for ensuring client satisfaction and resolving any issues that arise. Strong communication, problem-solving skills, and the ability to build long-term relationships are key to this role.",
        "Financial Controller":"A Financial Controller oversees the financial operations of an organization, ensuring that financial records are accurate, regulatory requirements are met, and financial reports are timely. Responsibilities include budgeting, forecasting, and auditing financial activities, as well as advising management on financial strategies. Strong accounting knowledge, leadership skills, and attention to detail are essential for this role.",
        "Risk Manager":"A Risk Manager is responsible for identifying and managing risks that could affect the organization’s operations, reputation, or profitability. This role involves developing risk management strategies, conducting risk assessments, and implementing mitigation measures. Risk Managers work closely with other departments to ensure that risks are appropriately managed. Analytical skills, problem-solving abilities, and knowledge of industry regulations are crucial for success in this role.",
        "Supply Chain Manager":"A Supply Chain Manager is responsible for overseeing the entire supply chain process, from raw material procurement to the final delivery of products to customers. This involves managing inventory, coordinating with suppliers, optimizing logistics, and ensuring timely delivery. Supply Chain Managers work closely with procurement, manufacturing, and distribution teams to streamline processes and reduce costs. Strong analytical skills, negotiation abilities, and knowledge of supply chain management software are essential for this role.",
        "Healthcare Administrator":"A Healthcare Administrator manages the day-to-day operations of healthcare facilities, such as hospitals, clinics, or nursing homes. The role involves overseeing staff, budgeting, ensuring compliance with healthcare regulations, and improving patient care services. Healthcare Administrators work closely with medical and support staff to ensure the facility operates smoothly. Organizational, communication, and leadership skills are crucial for success in this role.",
        "Research Scientist":"A Research Scientist conducts scientific studies and experiments to advance knowledge in a particular field. The role involves designing experiments, analyzing data, and publishing findings in scientific journals. Research Scientists may work in various industries, including pharmaceuticals, environmental science, and technology. Strong analytical skills, knowledge of scientific methods, and expertise in laboratory techniques are essential for this role.",
        "Pharmaceutical Sales Representative":"A Pharmaceutical Sales Representative promotes and sells pharmaceutical products to healthcare providers, hospitals, and pharmacies. The role involves building relationships with doctors and pharmacists, providing product information, and ensuring that sales targets are met. Knowledge of medical terminology, strong communication skills, and the ability to influence decision-makers are essential for this role.",
        "Real Estate Agent":"A Real Estate Agent helps clients buy, sell, or rent properties. The role involves advising clients on property values, showing properties, negotiating deals, and guiding clients through the buying or selling process. Strong interpersonal skills, knowledge of the local real estate market, and the ability to handle paperwork and legal documents are crucial for success in this role.",
        "Executive Assistant":"An Executive Assistant provides administrative support to high-level executives, managing their schedules, meetings, and correspondence. The role involves organizing travel arrangements, preparing reports, and handling confidential information. Strong organizational, communication, and multitasking abilities are essential for this role.",
        "Administrative Assistant":"An Administrative Assistant provides support to office staff by managing schedules, answering phone calls, handling correspondence, and performing clerical tasks. The role may also involve organizing meetings and maintaining office supplies. Strong organizational skills, attention to detail, and proficiency in office software are key to success in this role.",
        "Management Consultant":"A Management Consultant helps organizations improve their performance by analyzing existing business problems and developing solutions. The role involves conducting research, interviewing stakeholders, and presenting recommendations to management. Analytical skills, problem-solving abilities, and expertise in business operations are essential for this role.",
        "Construction Manager":"A Construction Manager oversees construction projects, from initial planning to final completion. This role involves managing teams of construction workers, ensuring safety standards are met, coordinating with contractors, and ensuring that projects are completed on time and within budget. Strong leadership, project management skills, and knowledge of construction methods are crucial for this role.",
        "Logistics Manager":"A Logistics Manager is responsible for managing the flow of goods, services, and information within an organization. This includes overseeing transportation, warehousing, inventory management, and ensuring the timely delivery of products. Strong organizational skills, attention to detail, and an understanding of logistics software are essential for this role.",
        "Procurement Manager":"A Procurement Manager is responsible for sourcing and purchasing goods and services for an organization. The role involves managing supplier relationships, negotiating contracts, and ensuring that the company’s purchasing requirements are met efficiently and cost-effectively. Strong negotiation skills, vendor management experience, and an understanding of procurement software are crucial for this role.",
        "Environmental Consultant":"An Environmental Consultant provides expert advice on environmental regulations, sustainability practices, and environmental risk assessments. The role involves conducting environmental audits, ensuring compliance with regulations, and recommending strategies for minimizing environmental impact. A background in environmental science, strong analytical skills, and knowledge of environmental laws are essential for this role.",
        "Education Consultant":"An Education Consultant provides guidance to schools, educational institutions, and parents on educational practices, policies, and strategies. This role involves helping institutions improve their academic programs, advising on curriculum development, and recommending solutions for educational challenges. Strong communication, knowledge of educational trends, and problem-solving abilities are crucial for success in this role.",
    }

    return job_descriptions