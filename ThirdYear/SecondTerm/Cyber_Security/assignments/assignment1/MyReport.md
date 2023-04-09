# Privacy and Security in the Cloud
## Paper overview
* This paper mainly talk about 4 main topics
  1. Introduction to the clouds, what they are? and how they work?
  2. Detailed analysis on the challenges that faces the cloud security, and what are the requirments needed for protecting the cloud privacy?
  3. Technologies used in the data encryption and the protection methods used. 
  4. Discussion on several research topics of data security for cloud storage. 
### Introduction to the clouds, what they are? and how they work?
* In our era, IOT now has a huge concern, everything now can be connected to internet, and we can build smart cities and smart homes.
* there is an estimation that by 2025, there will bee about 41.6 billion IOT devices or things generating 80 zettabytes (2^70) of data.   
* with such amount of data, the importance of the cloud storage is increasing, and the cloud storage is becoming a necessity for the future.
* clouds are a cloud computing centers, which allows enterprises to store and share their data in a remote location, and access it from anywhere via internet.
* This makes the enterprises has more agility and flexibility to access their data. 
* clouds promotes the integeration between bigdata, IOT and AI.
* their are six main advantages of the clouds
  1. unlimited data storage space
  2. convenient
  3. safe
  4. efficient file accessiblity
  5. offsite backup
  6. low cost of use
* there are main 5 categories of cloud storage
  1. public cloud
     - In this part there is an enterprise which want to store its data, so it outsource its data to a cloud service provider, and the cloud service provider will provide the enterprise with a virtual machine, and the enterprise can store its data in the virtual machine, but here the enterprise is usually small or medium size, so it does not have an infrastructure for its data or staff for managing the data, so it totally depends on the cloud service provider for managing its data and its security. 
  2. private cloud
     - Similar to the public cloud, except that the enterprise is usually a big one, so it wants to keed the security of its data, so it hire a staff which is responsible for managing and building an infrastructure for its cloud and keep their data secure, but this increases the cost drammaically, but it enhances the privace alot. 
  3. hybrid cloud
     - it is a combination of the public and the private cloud, so the enterprise can use the public cloud for unimportant data, and the private cloud for the rest of its sensitive data, so it combine the advantage of both.
  4. community cloud
     - it is mainly designed for enterprises which shares the same concerns and fields, so they can share their data and resources with each other, and they can also share the cost of the cloud service provider.
  5. personal cloud
     - it is designed for indviduals, so they can store their data in the cloud, and access it from anywhere, and they can also share their data with their friends and family.
* there are 3 main types of cloud services
  1. Infrastructure as a service (IaaS)
     - it is the lowest level of cloud services, and it is mainly used for building the infrastructure of the
  2. Platform as a service (PaaS)
     - it is the middle level of cloud services, and it is mainly used for building the applications of the cloud.
  3. Software as a service (SaaS)
     - it is the highest level of cloud services, and it is mainly used for using the applications of the cloud.
* From the Storage Prespective there are 3 main types of clouds
  1. Block Storage:
     - As the name suggests, block storage breaks up information and stores it in blocks that contain anywhere from 256 KB to 4 MB of data. The blocks aren’t organized hierarchically—in fact, they’re placed on the storage device in random order. That doesn’t slow down access, however, because each block has a unique identifier to distinguish it from every other block.

     -  When an application needs a file, it sends a request to the block storage system and the system gathers up all the relevant blocks quickly and efficiently, then assembles them into the complete file. Part of what makes block storage so fast is that it doesn’t use any metadata except for the unique identifier for each block. That makes block storage very efficient because data can take up almost the entire capacity, instead of having to make room for storing metadata.
      - Because of its speed, organizations use block storage when they need fast scale-up and speedy read/write performance.  
  2. File Storage:

      - it is a type of data storage that is hierarchical. If you’ve ever created or organized folders on a PC, you’ve used file storage. Also called file-level or file-based storage, this type is organized into files that are placed into folders and subfolders, which are located in a directory. It’s the type most often used to store information on a computer hard drive or on a device for network-attached storage (NAS) and is best used for quick in-and-out data storage and access.

       -   samilar to that on your PC, you store data in form of hirarchy
            >  ie: C:\Gihub\File1\text.txt 
  3. Object Storage: 
     -   data is stored as distinct objects. Each object has a unique identifier number and metadata. Object storage is flat, meaning it isn’t based on a hierarchy. It’s also API-friendly, which makes it easy to use with existing applications and systems, and extremely scalable. It’s the storage type of choice for many public cloud storage providers, such as AWS S3, as well as organizations with on-premises storage solutions.

     - Metadata is very important in object storage. Users can include a lot of details in the metadata, such as creator information, keywords, and even security and privacy policies and rules of access. Although objects are stored in a large pool, the unique identifiers and metadata make it simple—and speedy—to access any amount of data when it’s needed. 

     - Object storage, more than any other type, is well-suited to today’s massive volumes of data. This data is typically unstructured and difficult to organize in any hierarchical way (think social media content, videos, emails, sensor data from traffic lights, weather satellite images, and more).

     - Scalability is object storage’s main strength. Even when data grows to petabyte and exabytes, all of the objects are located in one namespace. And even though that namespace might be spread across hundreds of hardware devices and locations, the system can quickly access any and every object when it’s needed.
* Cloud storage is based on virtualization, so it consists of 4 main layers which are:
  1. Storage layer
  2. Primary Managment layer
  3. Application interface layer
  4. Access layer
* Due to all these characterstics of the cloud storage, we have to have a concern about the privace and security of the data, and the requirments for the data security in the clouds are mainly shown in these aspects:
  1. Data confidentiality
     -  ensure that the data is not accessible to unauthorized users. 
  2. Data integrity
     -  ensure that the data is not modified by unauthorized users. 
  3. Data availability
     -  ensure that any authorized user can access the data at any time. 
  4. Leakage resistance
     -  ensure that the data is not leaked to unauthorized users. 
  5. Privacy Protection
     -  ensure that the data is protected from the cloud providers themselves, so no one of the employees can access other companies data.  
  6. completly data deletion
     -  ensure that the data is deleted completely from the cloud, so no one can access it if the enterprise decided to delete them from the cloud. 
## The problem that the paper solves
* It tries to solve how to secure the data which are stored in the cloud by using some encryption technologies.
* Also It presents a comprehensive review on literature on data security, privacy issues and data encryption technologies. 

## The basic directions of the related work so far in the literature
* 

## The paper scientific contribution ( what is the added value of the paper?)
*


## My evaluation to the paper (My opinion about the paper)
*