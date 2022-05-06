#include <iostream>
#include "pastemyst.h"

// Sample PastyCreateInfo
const std::vector<PastyCreateInfo> newSamplePasties {
    {
        "New Sample Pasty Title",
        "New Sample Pasty Content",
        "AutoDetect"
    },
    {
        "New Second Sample Pasty Title",
        "New Second Sample Pasty Content",
        "AutoDetect"
    }
    // ... 
};

// Sample private PasteCreateInfo
PasteCreateInfo newSamplePasteCreateInfo{
    "New Sample Paste Title", "1h",
    true, false, "sample, private, paste",
    newSamplePasties
};

// Sample pastemyst username
const auto sampleUserName = "billyeatcookies";

int main()
{
    std::cout << "PasteMyst-CPP Example Project" << std::endl << std::endl;

    // Creating a new backend client instance.
    // can also do `Client client("token");`
    Client client;
    client.Authorize("token here");

#pragma region PasteEndpointMethods

    // Checking whether a Paste exists.
    std::cout << "Checking whether a Paste exists Before Fetching" << std::endl
        << ((client.PasteExists("99is6n23"))
            ? "  Paste exists"
            : "  Paste doesn't exist")
        << std::endl;

    // Fetching a Paste.
    auto fetchedPaste = client.GetPaste("99is6n23");
    std::cout << "Fetching the Paste" << std::endl
        << "  Paste Title: " << fetchedPaste.title << std::endl
        << "  Paste expiresIn: " << fetchedPaste.expiresIn
        << std::endl;

    // Creating a new private Paste.
    auto newPaste = client.CreatePaste(newSamplePasteCreateInfo);
    auto newPasteID = newPaste._id;
    std::cout << "Creating new private Paste" << std::endl
        << "  Created Paste ID: " << newPasteID << std::endl
        << "  Paste expiresIn: " << newPaste.expiresIn
        << std::endl;

    newPaste.title = "editedtitle";

    // Editing the paste just created.
    newPaste = client.EditPaste(newPasteID, newPaste);
    newPasteID = newPaste._id;
    std::cout << "Editing the created private Paste" << std::endl
        << "  Edited Paste's ID: " << newPasteID << std::endl
        << "  Edited Paste's title: " << newPaste.title
        << std::endl;

    // Deleting the created paste.
    std::cout << "Deleting the created-edited private Paste" << std::endl
        << ((client.DeletePaste(newPasteID))
            ? "  Paste Deleted Successfully"
            : "  Failed to Delete Paste")
        << std::endl;

#pragma endregion

    return 0;
}