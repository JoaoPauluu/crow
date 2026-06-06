import { useState, type MouseEvent } from "react";

interface ListGroupItem {
    id: number;
    name: string;
    OnClick?: (event: MouseEvent) => void;
}

interface ListGroupProps {
    listName?: string;
    items: ListGroupItem[];
}



function ListGroup({ listName = "", items }: ListGroupProps) {
    const [selectedIndex, setSelectedIndex] = useState(-1);


    const GenerateItem = (item:ListGroupItem) => {
        return (
            <li key={item.id}
                className={selectedIndex === item.id ? "list-group-item list-group-item-action active" : "list-group-item list-group-item-action"}
                onClick={(event) => {
                    setSelectedIndex(item.id);
                    if (item.OnClick) {item.OnClick(event)
                    }
                }}
            >
                    {item.name}
            </li>
        )
    }


    return (
        <>
            {listName && <h1>{listName}</h1>}
            <ul className="list-group">
                {items.length == 0 ? <li className="list-group-item">No items available</li> : items.map((item) => (
                    GenerateItem(item)
                ))}
            </ul>
        </>
    )
}

export default ListGroup;